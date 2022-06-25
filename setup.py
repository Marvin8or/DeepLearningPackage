#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='deep_learning_package_from_scratch',
    version='0.1.0',
    description="A simple package to build and train neural networks",
    long_description=readme + '\n\n' + history,
    author="Gabriel Marvin",
    author_email='gabrielmarvin18',
    url='https://github.com/Marvin8or/deep_learning_package_from_scratch',
    packages=[
        'deep_learning_package_from_scratch',
    ],
    package_dir={'deep_learning_package_from_scratch':
                 'deep_learning_package_from_scratch'},
    entry_points={
        'console_scripts': [
            'deep_learning_package_from_scratch=deep_learning_package_from_scratch.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='deep_learning_package_from_scratch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
