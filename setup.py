#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
"""Install script for this package."""

from setuptools import setup, find_packages

setup(
    name = "global_racetrajectory_optimization",
    version = "0.0.0",
    author = "Alexander Heilmeier",
    author_email = "alexander.heilmeier@tum.de",
    description = ("Generating global racetrajectories."),
    license = "LGPLv3",
    keywords = "",
    url = "https://github.com/TUMFTM/global_racetrajectory_optimization",
    packages=find_packages(),
    # long_description=read('README'),
    classifiers=[
        "Programming Language :: Python",
    ],
    install_requires=[
    ],
    # python_requires='>=3.6',
    extras_require={
    },
    scripts=[
        "main_gen_frictionmap.py",
        "main_globaltraj.py",
    ],
)
