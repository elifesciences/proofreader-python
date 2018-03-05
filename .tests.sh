#!/bin/bash

set -e

python setup.py install

pip install -r dev_requirements.txt

proofreader --targets proofreader tests

coverage run -m pytest --junitxml=build/pytest.xml
