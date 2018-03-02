import os

CONFIG_DIRECTORY = os.path.dirname(__file__)

PYLINT_CONFIG_NAME = '.pylintrc'
FLAKE8_CONFIG_NAME = '.flake8'
LICENSE_CHECKER_CONFIG_NAME = '.licenses_whitelist.txt'

DEFAULT_PYLINT_CONFIG_PATH = os.path.join(CONFIG_DIRECTORY, PYLINT_CONFIG_NAME)
DEFAULT_FLAKE8_CONFIG_PATH = os.path.join(CONFIG_DIRECTORY, FLAKE8_CONFIG_NAME)
DEFAULT_LICENSE_CHECKER_CONFIG_PATH = os.path.join(CONFIG_DIRECTORY, LICENSE_CHECKER_CONFIG_NAME)
