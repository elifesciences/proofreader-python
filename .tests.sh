#!/bin/bash

set -e

python setup.py install

pip install -r dev_requirements.txt

python -m proofreader proofreader tests

coverage run -m pytest --junitxml=build/pytest.xml
