from setuptools import setup

import proofreader


DEFAULT_DEPENDENCIES = (
    'flake8==3.5.0',
    'pylint==1.8.2',
)


try:
    with open('requirements.txt') as requirements_file:
        DEPENDENCIES = requirements_file.readlines()
except IOError:
    DEPENDENCIES = DEFAULT_DEPENDENCIES


setup(
    name='proofreader',
    version=proofreader.__version__,
    description='Utility for running both Pylint & Flake8 on targets whilst providing '
                'global, though overridable, defaults.',
    packages=['proofreader',
              'proofreader.config',
              'proofreader.license_checker',
              'proofreader.utils'],
    include_package_data=True,
    install_requires=DEPENDENCIES,
    license='MIT',
    url='https://github.com/elifesciences/proofreader-python.git',
    maintainer='eLife Sciences Publications Ltd.',
    maintainer_email='tech-team@elifesciences.org',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        'console_scripts': [
            'proofreader=proofreader.__main__:main',
        ],
    },

)

