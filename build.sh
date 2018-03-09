#!/bin/bash
set -e

.tox/py35/bin/python setup.py sdist bdist_wheel

