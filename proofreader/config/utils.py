import os

from proofreader.config import (
    DEFAULT_FLAKE8_CONFIG_PATH,
    DEFAULT_PYLINT_CONFIG_PATH,
    DEFAULT_LICENSE_CHECKER_CONFIG_PATH,
    FLAKE8_CONFIG_NAME,
    LICENSE_CHECKER_CONFIG_NAME,
    PYLINT_CONFIG_NAME,
)


def get_flake8_options(config_dir='.'):
    # type: (str) -> List[str]
    """Checks for local config overrides for `flake8`
    and add them in the correct `flake8` `options` format.

    :param config_dir:
    :return: List[str]
    """
    if FLAKE8_CONFIG_NAME in os.listdir(config_dir):
        flake8_config_path = FLAKE8_CONFIG_NAME
    else:
        flake8_config_path = DEFAULT_FLAKE8_CONFIG_PATH

    return ['--config={}'.format(flake8_config_path)]


def get_license_checker_config_path(config_dir='.'):
    # type: (str) -> List[str]
    """Checks for local config overrides for license checker,
    if not found it returns the package default.

    :param config_dir:
    :return: str
    """
    if LICENSE_CHECKER_CONFIG_NAME in os.listdir(config_dir):
        license_checker_config_path = LICENSE_CHECKER_CONFIG_NAME
    else:
        license_checker_config_path = DEFAULT_LICENSE_CHECKER_CONFIG_PATH

    return license_checker_config_path


def get_pylint_options(config_dir='.'):
    # type: (str) -> List[str]
    """Checks for local config overrides for `pylint`
    and add them in the correct `pylint` `options` format.

    :param config_dir:
    :return: List [str]
    """
    if PYLINT_CONFIG_NAME in os.listdir(config_dir):
        pylint_config_path = PYLINT_CONFIG_NAME
    else:
        pylint_config_path = DEFAULT_PYLINT_CONFIG_PATH

    return ['--rcfile={}'.format(pylint_config_path)]
