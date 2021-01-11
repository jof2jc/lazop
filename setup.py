# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in lazop/__init__.py
from lazop import __version__ as version

setup(
	name='lazop',
	version=version,
	description='Lazada SDK',
	author='Lazada',
	author_email='jof2jc@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
