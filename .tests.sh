#!/bin/bash

set -e

python setup.py install

python -m proofreader proofreader tests

coverage run -m pytest --junitxml=build/pytest.xml
