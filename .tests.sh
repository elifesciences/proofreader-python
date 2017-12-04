#!/usr/bin/env bash

set -e

pip install --requirement requirements.txt

python setup.py install

python -m proofreader proofreader tests

coverage run -m pytest --junitxml=build/pytest.xml
