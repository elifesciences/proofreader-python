try:
    from unittest.mock import MagicMock
except ImportError:  # pragma: no cover
    from mock import MagicMock

from pytest import fixture

from proofreader.license_checker.package import Package


@fixture
def bad_py_text():
    return ['import os, sys\n', '\n', '\n',
            'def SomeInvalidName():\n', '    pass\n']


@fixture
def builtin_fail_text():
    return ['def my_method(object, list, dict):\n',
            '    max = 5\n', '    min = 3\n', '    zip = (4, 3)\n']


@fixture
def good_py_text():
    return ['"""\n', 'A good py\n',
            '"""\n', '\n', '\n', 'def foobar():\n',
            '    """This is a function"""\n',
            "    return 'bar'\n"]


@fixture
def good_py_file(tmpdir, good_py_text):
    py_file = tmpdir.mkdir('dummy').join('good.py')
    py_file.write(''.join(good_py_text))
    return py_file


@fixture
def builtin_fail_py_file(tmpdir, good_py_text):
    py_file = tmpdir.mkdir('dummy').join('good.py')
    py_file.write(''.join(good_py_text))
    return py_file


@fixture
def bad_py_file(tmpdir, bad_py_text):
    py_file = tmpdir.mkdir('dummy').join('bad.py')
    py_file.write(''.join(bad_py_text))
    return py_file


@fixture
def mock_pkg():
    return MagicMock()


@fixture
def package_with_license(mock_pkg):
    mock_pkg.get_metadata_lines.return_value = ['License: MIT']
    return Package(pkg_obj=mock_pkg)


@fixture
def package_with_name(mock_pkg):
    mock_pkg.get_metadata_lines.return_value = ['Name: some package']
    return Package(pkg_obj=mock_pkg)


@fixture
def package_with_version(mock_pkg):
    mock_pkg.version = '1.0.0'
    return Package(pkg_obj=mock_pkg)


@fixture
def package_no_license(mock_pkg):
    mock_pkg.get_metadata_lines.return_value = []
    return Package(pkg_obj=mock_pkg)


@fixture
def package_no_version(mock_pkg):
    mock_pkg.version = ''
    return Package(pkg_obj=mock_pkg)


@fixture
def package_no_name(mock_pkg):
    mock_pkg.get_metadata_lines.return_value = []
    return Package(pkg_obj=mock_pkg)
