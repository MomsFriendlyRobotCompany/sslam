#!/usr/bin/env python
# -----------------------------------------------------------
# Copyright (C) 2018 Kevin J. Walchko
# Copyright (C) 2014 Simon D. Levy
# License: LGPL

from setuptools import setup, Extension
from platform import machine
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
import os

# from psutils
# this allows me to get version w/o importing because I get an import error
# for c_sslam which isn't compiled yet
def get_version(pkg):
	HERE = os.path.abspath(os.path.dirname(__file__))
	INIT = os.path.join(HERE, pkg + '/__init__.py')
	with open(INIT, 'r') as f:
		for line in f:
			if line.startswith('__version__'):
				ret = eval(line.strip().split(' = ')[1])
				assert ret.count('.') == 2, ret
				for num in ret.split('.'):
					assert num.isdigit(), ret
				return ret
		raise ValueError("couldn't find version string")

# Support streaming SIMD extensions

OPT_FLAGS  = []
SIMD_FLAGS = []

arch = machine()

if arch == 'i686':
	SIMD_FLAGS = ['-msse3']
elif arch == 'armv7l':
	OPT_FLAGS = ['-O3']
	SIMD_FLAGS = ['-mfpu=neon']
else:
	arch = 'sisd'

SOURCES = [
	'./c/c_sslam.c',
	'./c/pyextension_utils.c',
	'./c/coreslam.c',
	'./c/coreslam_' + arch + '.c',
	'./c/random.c',
	'./c/ziggurat.c']

module = Extension(
	'c_sslam',
	sources = SOURCES,
	extra_compile_args = SIMD_FLAGS + OPT_FLAGS
	)

PACKAGE_NAME = 'sslam'
VERSION = get_version(PACKAGE_NAME)
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
README = open('readme.md').read()

setup (
	name = PACKAGE_NAME,
	version = VERSION,
	description = 'Simple, efficient SLAM in Python',
	long_description=README,
	long_description_content_type="text/markdown",
	packages = [PACKAGE_NAME],
	keywords=['lidar'],
	author_email="walchko@users.noreply.github.com",
	ext_modules = [module],
	author='Kevin Walchko',
	url='http://github.com/MomsFriendlyRobotCompany/{}'.format(PACKAGE_NAME),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		# 'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	license='LGPL',
	install_requires=[
		'pyyaml',
		'pyserial',
		'build_utils',
		'simplejson'],
	platforms='Linux; OS X',
	cmdclass={
		'publish': PublishCommand,
		'make': BuildCommand
	}
)
