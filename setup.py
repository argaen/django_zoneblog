#!/usr/bin/env python

from setuptools import setup

packages = ['Django>=1.7', 'django-taggit']

setup(
    name='DjangoZone',
    version='1.0',
    description='DjangoZone blog app',
    author='Manuel Miranda',
    author_email='manu.mirandad@gmail.com',
    url='https://github.com/argaen/djangozone',
    install_requires=packages,
)
