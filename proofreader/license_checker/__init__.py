from __future__ import print_function
import os
import pkg_resources

from proofreader.license_checker.package import Package
from proofreader.utils.print_table import PrintTable


CONFIG_NAME = '.restricted_licenses.txt'
ROW_HEADERS = ['Package', 'Version', 'License', 'Can Use']


def _get_packages():
    # type: () -> List[Package]
    """Convert `pkg_resources.working_set` into a list of `Package` objects.

    :return: list
    """
    return [Package(pkg_obj=pkg) for pkg in sorted(pkg_resources.working_set,
                                                   key=lambda x: str(x).lower())]


def _get_restricted_licenses(config_path):
    # type: (str) -> List[str]
    """Get restricted license names from config file.

    :param config_path: str
    :return: list
    """

    restricted_licenses = []

    try:
        with open(config_path) as config:
            restricted_licenses = [line.rstrip() for line in config]
    except IOError:  # pragma: no cover
        print('Warning: No .restricted_licenses.txt file was found.')

    return restricted_licenses


def run_license_checker(config_dir):
    # type: (str) -> None
    """Generate table of installed packages and check for license
    warnings based off user defined restricted license values.

    :param config_dir:
    :return:
    """
    config_path = os.path.join(config_dir, CONFIG_NAME)
    table = PrintTable(ROW_HEADERS)
    restricted_licenses = _get_restricted_licenses(config_path)

    warnings = []

    for pkg in _get_packages():
        allowed = pkg.license not in restricted_licenses
        table.add_row((pkg.name, pkg.version, pkg.license, str(allowed)))

        if not allowed:
            warnings.append(pkg)

    print(table)

    print('{} RESTRICTED LICENSES DETECTED'.format(len(warnings)))
