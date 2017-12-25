import argparse

from parser import DependencyParser


argument_parser = argparse.ArgumentParser(description="""
    Get information if your dependent packages are Python 3 compatible yet
""".strip())
argument_parser.add_argument('-v', '--verbose',
    help="Display information about all packages in the requirements file",
    action='store_true', default=False
)
argument_parser.add_argument('--ignore',
    help="Prefixes of packages that you\'d like to ignore while parsing the file",
    nargs='*', default=[]
)
argument_parser.add_argument('filename',
    help="Name of the file that contains the dependencies",
)

def run():
    args = argument_parser.parse_args()
    dependency_parser = DependencyParser(args.ignore, args.verbose)
    dependency_parser.parse_file(args.filename)
