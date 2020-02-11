#!/bin/bash
set -e

.tox/py3/bin/python setup.py sdist bdist_wheel

