"""Main module for proofreader.

This module

- Takes `n` commandline arguments as `targets` and calls the runner.run function

"""
import os
import sys

from proofreader.runner import run

DIRECTORY = os.getcwd()

run(targets=sys.argv[1:], config_dir=DIRECTORY)
