# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(name='bug_hunt',
    install_requires = [
        'django>=1.8.0,<1.9',
    ],
    tests_require=[
        'django-selenium-clean',
    ],
)
