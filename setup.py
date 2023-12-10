#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='synth',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your project dependencies here
    ],
    scripts=['app/synthesize.py']
)
