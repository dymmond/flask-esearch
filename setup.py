#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-ESearch
-------------
Extension for Flask and ElasticSearch.
"""
import os
import sys
import re
from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='Flask-ESearch',
    version=find_version("src/__init__.py"),
    url='https://github.com/dymmond/flask-esearch',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Tiago Silva & Pedro Correia',
    author_email='mail@tiagoasilva.com',
    description='Extension of Elasticsearch for Flask with a simple integration',
    py_modules=['flask_esearch'],
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=1.1.2',
        'Elasticsearch>=6.4.6,<=7.7.1',
        'Elasticsearch-dsl>=6.4.6,<=7.2.1'
    ],
    classifiers=[
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
