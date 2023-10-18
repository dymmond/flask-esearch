#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-ESearch
-------------
Extension for Flask and ElasticSearch.
"""
import os
import re
import sys

from setuptools import find_packages, setup

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
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
    name="Flask-ESearch",
    version="0.5.0",
    url="https://github.com/dymmond/flask-esearch",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Tiago Silva",
    author_email="tiago.silva@dymmond.com",
    description="Extension of Elasticsearch for Flask with a simple integration",
    py_modules=["flask_esearch"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask>=2.3.0", "Elasticsearch>=6.4.6", "Elasticsearch-dsl>=6.4.6"],
    classifiers=[
        "Framework :: Flask",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
