elifeLibrary {
    stage 'Checkout', {
        checkout scm
    }

    stage 'Project tests', {
        elifeLocalTests "./project_tests.sh"
    }

    def candidateVersion
    stage 'Build', {
        sh './build.sh'
        candidateVersion = sh(script: ".tox/py35/bin/python -c 'import proofreader; print(proofreader.__version__)'", returnStdout: true).trim()
        echo "Candidate version: v${candidateVersion}"
    }

    elifeMainlineOnly {
        stage 'Push release', {
            def isNew = sh(script: "git tag | grep v${candidateVersion}", returnStatus: true) != 0
            if (isNew) {
                sh "git tag v${candidateVersion} && git push origin v${candidateVersion}"
                sh "twine upload dist/*"
            }
        }
    }
}
