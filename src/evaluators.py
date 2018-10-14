import requests


def is_ok_on_pypi(package_name, package_version=None):
    response = requests.get('https://pypi.python.org/pypi/{package_name}/{package_version}'.format(
        package_name=package_name,
        package_version='' if package_version is None else package_version
    ))
    return 'Python :: 3' in response.content
