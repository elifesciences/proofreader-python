"""Module `runner`

This module

- checks for local config overrides
- runs `flake8` and `pylint` on the
- optionally runs license_checker
- outputs run_command progress to stdout and stderr
- returns exit code based on the success or failure of both commands

"""
from __future__ import print_function
from subprocess import Popen
import sys

from proofreader.config.utils import (
    get_flake8_options,
    get_pylint_options,
    get_license_checker_config_path,
)
from proofreader.license_checker import run_license_checker


def run(targets, config_dir='.', check_licenses=False):
    # type: (List[str], str, bool) -> None
    """Runs `pylint` and `flake8` commands and exits based off the evaluation
    of both command results.

    :param targets: List[str]
    :param config_dir: str
    :param check_licenses: bool
    :return:
    """
    pylint_return_state = False
    flake8_return_state = False

    if check_licenses:
        run_license_checker(config_path=get_license_checker_config_path(config_dir))

    pylint_options = get_pylint_options(config_dir=config_dir)
    flake8_options = get_flake8_options(config_dir=config_dir)

    if targets:
        pylint_return_state = _run_command(command='pylint', targets=targets,
                                           options=pylint_options)
        flake8_return_state = _run_command(command='flake8', targets=targets,
                                           options=flake8_options)

    if not flake8_return_state and not pylint_return_state:
        sys.exit(0)
    else:
        sys.exit(1)


def _run_command(command, targets, options):
    # type: (str, List[str], List[str]) -> bool
    """Runs `command` + `targets` + `options` in a
    subprocess and returns a boolean determined by the
    process return code.

    >>> result = run_command('pylint', ['foo.py', 'some_module'], ['-E'])
    >>> result
    True

    :param command: str
    :param targets: List[str]
    :param options: List[str]
    :return: bool
    """
    print('{0}: targets={1} options={2}'.format(command, targets, options))
    cmd = [command] + targets + options
    process = Popen(cmd)
    process.wait()

    return bool(process.returncode)
