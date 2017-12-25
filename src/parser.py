from evaluators import is_ok_on_pypi


class DependencyParser(object):

    def __init__(self, ignored_prefixes=None, verbose=False):
        self.ignored_prefixes = ignored_prefixes
        self.verbose = verbose

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.parse_line(line.strip())

    def parse_line(self, line):
        if not len(line) or line.startswith('#'):
            return

        if any([line.startswith(prefix) for prefix in self.ignored_prefixes]):
            return

        package_name, package_version = line.split('==')
        pypi_looks_good = is_ok_on_pypi(package_name, package_version)
        if not pypi_looks_good or self.verbose:
            print('{indicator}-{package_name}@{package_version}'.format(
                indicator='OK' if pypi_looks_good else 'NO',
                package_name=package_name,
                package_version=package_version
            ))
