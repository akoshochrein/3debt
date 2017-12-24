import argparse
import requests


parser = argparse.ArgumentParser(description="""
    Get information if your packages are Python 3 compatible yet
""".strip())

parser.add_argument('filename',
    help='Name of the file that contains the dependencies'
)

def run():
    args = parser.parse_args()
    parse_file(args.filename)


def parse_file(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            parse_line(line.strip())


def parse_line(line):
    if not len(line) or line.startswith('#'):
        return
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
