#!/usr/bin/env python

from setuptools import setup, find_packages
import os

# Code From: https://pythonhosted.org/an_example_pypi_project/setuptools.html
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


REQUIREMENTS = ['contracts']
EXCLUDE_FROM_PACKAGES = []

setup(
    name='diskspace',
    version='0.0.1',
    url='https://github.com/TecProg-20181/04-diskspace-Mateusas3s',
    author='Mateus Augusto Sousa e Silva',
    author_email='mateusaugusto-2009@hotmail.com',
    description='Command to analyze how much each file occupies in a folder',
    license='LICENSE.txt',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points={'console_scripts': [
        'diskspace = diskspace.diskspace:main',
    ]},
    long_description=read('README.md'),
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Shells',
    ],
)
