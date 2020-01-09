#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

unparsed_requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in unparsed_requirements]

setup(name='sif',
      version='0.0.1',
      description='This package has shared components.',
      author='Sanjeev Arora and Yingyu Liang and Tengyu Ma and Philipp Hager',
      author_email='',
      packages=find_packages(exclude=["examples*", "data*", "auxiliary_data*"]),
      license='LICENSE',
      install_requires=requirements
      )
