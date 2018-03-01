import pkg_resources
import prettytable


# TODO available licenses model


class Package(object):
    license = ''
    name = ''
    version = ''

    def __init__(self, pkg_obj):
        self.pkg_obj = pkg_obj



def get_pkg_license(pkg):
    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')

    for line in lines:
        if line.startswith('License:'):
            return line[9:]
    return '(Licence not found)'


def get_pkg_name(pkg):
    try:
        lines = pkg.get_metadata_lines('METADATA')
    except:
        lines = pkg.get_metadata_lines('PKG-INFO')

    for line in lines:
        if line.startswith('Name:'):
            return line[6:]
    return '(Name not found)'


def get_pkg_version(pkg):
    return pkg.version or ''


def print_packages_and_licenses():
    t = prettytable.PrettyTable(['Package', 'Version', 'License', 'Can Use'])

    # get a package by name
    packages = pkg_resources.working_set

    # for p in packages:
    #     print(type(p))  # <class 'pkg_resources.DistInfoDistribution'>

    for pkg in sorted(packages, key=lambda x: str(x).lower()):
        t.add_row((get_pkg_name(pkg), get_pkg_version(pkg), get_pkg_license(pkg), 'yes'))

    print(t)
