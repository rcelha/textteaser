#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

cwd = path.dirname(path.realpath(__file__))
with open(path.join(cwd, 'README.md')) as f:
    long_description = f.read()

setup(
  name="textteaser",
  version="1.0.0",
  description='TextTeaser is an automatic summarization algorithm',
  long_description=long_description,
  url='https://github.com/rcelha/textteaser',
  install_requires=['nltk'],
  packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
