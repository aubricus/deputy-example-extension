#!/usr/bin/env python

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'ext'
]

package_data = {'ext': ['LICENSE.md', 'README.md']}

requires = [
    'setuptools',
    'docopt==0.6.1'
]

entry_points = {
    'console_scripts': ['ext = ext.cli:main']
}

setup(
    url='http://github.com/aubricus/ext',
    name='ext',
    version='0.0.0u',
    description='Lorem ipsum dolor.',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir={'ext': 'ext'},
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),

)

del os.environ['PYTHONDONTWRITEBYTECODE']
