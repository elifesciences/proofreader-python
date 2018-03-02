from __future__ import print_function
import pkg_resources

from proofreader.config.utils import LICENSE_CHECKER_CONFIG_NAME
from proofreader.license_checker.package import Package
from proofreader.utils.print_table import PrintTable


ROW_HEADERS = ['Package', 'Version', 'License', 'Can Use']


def _get_packages():
    # type: () -> List[Package]
    """Convert `pkg_resources.working_set` into a list of `Package` objects.

    :return: list
    """
    return [Package(pkg_obj=pkg) for pkg in sorted(pkg_resources.working_set,
                                                   key=lambda x: str(x).lower())]


def _get_whitelist_licenses(config_path):
    # type: (str) -> List[str]
    """Get whitelist license names from config file.

    :param config_path: str
    :return: list
    """

    whitelist_licenses = []

    try:
        print('config path', config_path)
        with open(config_path) as config:
            whitelist_licenses = [line.rstrip() for line in config]
    except IOError:  # pragma: no cover
        print('Warning: No {} file was found.'.format(LICENSE_CHECKER_CONFIG_NAME))

    return whitelist_licenses


def run_license_checker(config_path):
    # type: (str) -> None
    """Generate table of installed packages and check for license
    warnings based off user defined restricted license values.

    :param config_path: str
    :return:
    """
    whitelist_licenses = _get_whitelist_licenses(config_path)
    table = PrintTable(ROW_HEADERS)

    warnings = []

    for pkg in _get_packages():
        allowed = pkg.license in whitelist_licenses
        table.add_row((pkg.name, pkg.version, pkg.license, str(allowed)))

        if not allowed:
            warnings.append(pkg)

    print(table)

    print('{} RESTRICTED LICENSES DETECTED'.format(len(warnings)))
