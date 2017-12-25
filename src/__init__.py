import argparse
import requests


parser = argparse.ArgumentParser(description="""
    Get information if your dependent packages are Python 3 compatible yet
""".strip())
parser.add_argument('-v', '--verbose',
    help="Display information about all packages in the requirements file",
    action='store_true', default=False
)
parser.add_argument('--ignore',
    help="Prefixes of packages that you\'d like to ignore while parsing the file",
    nargs='*', default=[]
)
parser.add_argument('filename',
    help="Name of the file that contains the dependencies",
)

def run():
    args = parser.parse_args()
    parse_file(args.filename, args.ignore, args.verbose)


def parse_file(filename, ignored_prefixes, verbose):
    with open(filename, 'r') as f:
        for line in f.readlines():
            parse_line(line.strip(), ignored_prefixes, verbose)


def parse_line(line, ignored_prefixes, verbose):
    if not len(line) or line.startswith('#'):
        return

    if any([line.startswith(prefix) for prefix in ignored_prefixes]):
        return

    package_name, package_version = line.split('==')
    if not is_package_3_good(package_name, package_version) or verbose:
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
