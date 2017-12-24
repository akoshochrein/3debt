from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='3debt',
    version='0.0.1',
    description='Python 3 dependency checker',
    long_description=long_description,
    url='https://github.com/akoskaaa/3debt',
    author_email='hoch.akos@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            '3debt=src:run',
        ],
    },
)