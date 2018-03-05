import argparse
import os

from proofreader.runner import run

DIRECTORY = os.getcwd()

PARSER = argparse.ArgumentParser(description='proofreader')

PARSER.add_argument('--check-licenses', type=bool, help='Check for supported licenses .e.g. true')
PARSER.add_argument('--targets', default=[], nargs='*',
                    help='Target files and directories .e.g. dir1/* file1.py file2.py')

ARGS = PARSER.parse_args()


def main():
    run(targets=ARGS.targets, config_dir=DIRECTORY, check_licenses=ARGS.check_licenses)
