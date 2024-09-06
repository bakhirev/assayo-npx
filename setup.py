#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python-m twine upload dist/*  # 'twine' must be installed: 'pip install twine'


import ast
import io
import os
from glob import glob
from setuptools import find_packages, setup

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = []
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="assayo",
    version="0.0.4",
    author="Aleksei Bakhirev",
    author_email="alexey-bakhirev@yandex.ru",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bakhirev/assayo-npx",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    entry_points={"console_scripts": ["assayo=bin.main:main"]},
    zip_safe=False,
    package_data = {"assayo":["assayo/**/*"]},
    install_requires=DEPENDENCIES,
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        # "Operating System :: OS Independent",
        # "Private :: Do Not Upload"
    ],
)