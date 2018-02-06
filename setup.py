from setuptools import setup

import proofreader


with open('requirements.txt') as requirements_file:
    DEPENDENCIES = requirements_file.readlines()


setup(
    name='proofreader',
    version=proofreader.__version__,
    description='Utility for running both Pylint & Flake8 on targets whilst providing '
                'global, though overridable, defaults.',
    packages=['proofreader', 'proofreader.config'],
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
    ]

)

