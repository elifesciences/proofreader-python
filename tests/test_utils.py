try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import pytest

from proofreader.config.utils import (
    FLAKE8_CONFIG_NAME,
    PYLINT_CONFIG_NAME,
    get_flake8_options,
    get_pylint_options
)


def test_it_can_provide_default_flake8_options():
    options = get_flake8_options()
    assert len(options) == 1
    assert '--config' in options[0]


def test_it_can_provide_default_pylint_options():
    options = get_pylint_options()
    assert len(options) == 1
    assert '--rcfile' in options[0]


@patch('proofreader.config.os.listdir')
def test_it_can_provide_custom_flake8_config(mock_listdir):
    mock_listdir.return_value = [FLAKE8_CONFIG_NAME]

    options = get_flake8_options('custom_path')
    assert len(options) == 1
    assert options[0] == '--config={}'.format(FLAKE8_CONFIG_NAME)


@patch('proofreader.config.os.listdir')
def test_it_can_provide_custom_pylint_config(mock_listdir):
    mock_listdir.return_value = [PYLINT_CONFIG_NAME]

    options = get_pylint_options('custom_path')
    assert len(options) == 1
    assert options[0] == '--rcfile={}'.format(PYLINT_CONFIG_NAME)


def test_it_raises_error_with_invalid_path_for_flake8_config():
    with pytest.raises(OSError):
        get_flake8_options('invalid_path')


def test_it_raises_error_with_invalid_path_for_pylint_config():
    with pytest.raises(OSError):
        get_pylint_options('invalid_path')
