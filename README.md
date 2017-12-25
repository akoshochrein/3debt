# 3debt
Try to figure out what dependencies you're missing to start upgrading your project to Python 3

## Installation
```
pip install -g 3debt
```

## Usage
```
3debt requirements.txt
```

```
$ 3debt -h
usage: 3debt [-h] [--ignore [IGNORE [IGNORE ...]]] filename

Get information if your dependent packages are Python 3 compatible yet

positional arguments:
  filename              Name of the file that contains the dependencies

optional arguments:
  -h, --help            show this help message and exit
  --ignore [IGNORE [IGNORE ...]]
                        Prefixes of packages that you'd like to ignore while
                        parsing the file
```
