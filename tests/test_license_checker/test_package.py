from proofreader.license_checker.package import Package


def test_can_create_package(mock_pkg):
    assert Package(pkg_obj=mock_pkg)


def test_can_get_package_license(package_with_license):
    assert package_with_license.license == 'MIT'


def test_will_handle_no_license_found(package_no_license):
    assert package_no_license.license == '* Not Found *'


def test_can_get_package_version(package_with_version):
    assert package_with_version.version == '1.0.0'


def test_will_get_blank_version_if_not_found(package_no_version):
    assert package_no_version.version == ''


def test_can_get_name(package_with_name):
    assert package_with_name.name == 'some package'


def test_will_handle_name_not_found(package_no_name):
    assert package_no_name.name == '* Not Found *'
