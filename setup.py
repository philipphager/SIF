#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='sif',
      version='0.0.1',
      description='This package has shared components.',
      author='Sanjeev Arora and Yingyu Liang and Tengyu Ma and Philipp Hager',
      author_email='',
      packages=find_packages(exclude=["examples*", "data*", "auxiliary_data*"]),
      license='LICENSE',
    )
