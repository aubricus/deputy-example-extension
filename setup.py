#!/usr/bin/env python

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'deputy_lib',
]

package_data = {'deputy_lib': ['LICENSE.md', 'README.md']}

requires = [
    'setuptools',
    'docopt==0.6.1',
]

entry_points = {
    'deputy.casefiles': [
        'bang=deputy_lib.bang',
        'bash=deputy_lib.bash',
        'pop=deputy_lib.pop',
    ]
}

setup(
    url='http://github.com/aubricus/deputy_lib',
    name='deputy_lib',
    version='0.0.0u',
    description='Lorem ipsum dolor.',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir={'deputy_lib': 'deputy_lib'},
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    zip_safe=False,
)

del os.environ['PYTHONDONTWRITEBYTECODE']
