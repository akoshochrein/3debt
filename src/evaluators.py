import requests


def is_ok_on_pypi(package_name, package_version):
    response = requests.get('https://pypi.python.org/pypi/{package_name}/{package_version}'.format(
        package_name=package_name,
        package_version=package_version
    ))
    return 'Programming Language :: Python :: 3' in response.content
