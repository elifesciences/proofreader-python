#!/bin/bash

tox
. .tox/py3/bin/activate

COVERALLS_REPO_TOKEN=$(cat /etc/coveralls/tokens/proofreader-python) coveralls
