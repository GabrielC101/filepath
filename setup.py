# Copyright (c) 2010 Jean-Paul Calderone
# See LICENSE file for details.

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
    long_description = f.read()

setup(
    name="filepath",
    description="Object-oriented filesystem path representation.",
    long_description=long_description,
    version="0.3",
    author="Twisted Matrix Labs",
    author_email="twisted-python@twistedmatrix.com",
    url="http://twistedmatrix.com/",
    packages=["filepath", "filepath.test"],
    install_requires=["zope.interface", "incremental"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Filesystems",
        ])
