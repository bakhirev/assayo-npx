#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
from setuptools import find_packages, setup

setup(
    name="assayo",
    version="0.0.9",
    author="Aleksei Bakhirev",
    author_email="alexey-bakhirev@yandex.ru",
    description="Visualization and analysis of git commit statistics. Team Lead performance tool.",
    url="https://github.com/bakhirev/assayo-npx",
    packages=["bin", "assayo"],
    package_dir={
        "bin": "bin",
        "assayo": "assayo",
    },
    keywords=["git","stat","statistic","statistics","log","report","audit","data-visualization","commit","commits","achivments"],
    scripts=[],
    entry_points={"console_scripts": ["assayo=bin.main:main"]},
    zip_safe=False,
    package_data = {"assayo":["assayo/**/*", "README.md"]},
    include_package_data=True,
    python_requires=">=3.6",
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        # "Operating System :: OS Independent",
        # "Private :: Do Not Upload"
    ],
)