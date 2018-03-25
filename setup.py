#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'scrapy>=1.5.0',
                'requests==2.18.4', 'furl==1.0.1']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Artem Ezhov",
    author_email='raystlin.bd@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description=("CLI утилита, основанная на Scrapy,"
                 " для загрузки обоев с сайта www.smashingmagazine.com"),
    entry_points={
        'console_scripts': [
            'sw-downloader=sw_downloader.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sw_downloader',
    name='sw_downloader',
    packages=find_packages(include=['sw_downloader']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/aezhov/sw_downloader',
    version='0.1.0',
    zip_safe=False,
)
