import requests


def run():
    parse_file('requirements.txt')


def parse_file(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            parse_line(line.strip())


def parse_line(line):
    package_name, package_version = line.split('==')
    print('{indicator}-{package_name}@{package_version}'.format(
        indicator='OK' if is_package_3_good(package_name, package_version) else 'NO',
        package_name=package_name,
        package_version=package_version
    ))


def is_package_3_good(package_name, package_version):
    response = requests.get('https://pypi.python.org/pypi/{package_name}/{package_version}'.format(
        package_name=package_name,
        package_version=package_version
    ))
    return 'Programming Language :: Python :: 3' in response.content
