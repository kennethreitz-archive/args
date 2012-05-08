# -*- coding: utf-8 -*-
"""
args
~~~~

This simple module gives you an elegant interface for your command line argumemnts.

"""

from setuptools import setup

setup(
    name='args',
    version='0.1.0',
    url='https://github.com/kennethreitz/args',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Command Arguments for Humans.',
    long_description=__doc__,
    py_modules=['args'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
