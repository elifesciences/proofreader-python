from setuptools import setup

import proofreader

setup(
    name='proofreader-python',
    version=proofreader.__version__,
    description='Utility for running both Pylint & Flake8 on targets whilst providing '
                'global, though overridable, defaults.',
    packages=['proofreader', 'proofreader.config'],
    package_data={
        'proofreader/config': '.*'
    },
    license='MIT',
    url='https://github.com/elifesciences/proofreader-python.git',
    maintainer='eLife Sciences Publications Ltd.',
    maintainer_email='tech-team@elifesciences.org',
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ]

)

