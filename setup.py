#!/usr/bin/env python3
from setuptools import setup, find_packages

import csiagent


setup(
    name = 'csiagent',
    version = csiagent.__version__,
    description = 'A simple Python 3 chat bot',
    license = 'MIT',
    author = 'Jonathan Zentgraf',
    author_email = 'zx96dev@gmail.com',
    url = 'https://github.com/rollforbugs/csiagent',
    packages = find_packages('.', exclude=['tests']),
    entry_points = {
        'console_scripts': [
            'csiagent = csiagent.__main__:main',
        ]
    },
)
