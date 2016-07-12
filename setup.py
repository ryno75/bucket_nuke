#!/usr/bin/env python

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 5):
    error = 'ERROR: bucket_nuke requires Python Version 2.6 or above...exiting.'
    print >> sys.stderr, error
    sys.exit(1)

def readme():
    with open('README.md') as fh:
        return fh.read()

def history():
    with open('HISTORY.md') as fh:
        return fh.read().replace('.. :changelog:', '')

VERSION = '0.1.0'
REQUIRES = [
    'argparse',
    'boto3'
]

setup(name = 'bucket_nuke',
    version = VERSION,
    description = 'Library for wiping S3 buckets',
    long_description = readme() + '\n\n' + history(),
    author = 'Ryan Kennedy',
    author_email = 'ryno75@gmail.com',
    scripts = ['bin/nuke_buckets'],
    url = 'https://github.com/ryno75/bucket_nuke.git',
    packages = ['bucket_nuke'],
    license = 'Apache 2.0',
    platforms = 'Posix; MacOS X; Windows',
    include_package_data=True,
    install_requires=REQUIRES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet'
    ]
)
