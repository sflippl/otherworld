#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on DATE Mon May 20 12:20:33 2019

@author: sflippl
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otherworld",
    version="0.1.0a0",
    author="Samuel Lippl",
    author_email="sfc.lippl@gmail.com",
    description="Perturb natural image statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sflippl/otherworld",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
