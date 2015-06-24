# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requires = [
    'django',
    'psycopg2',
]

develop_requires = [
]

setup(
    name='{{ project_name }}',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'develop': develop_requires,
    },
    zip_safe=False,
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.manage:main',
        ]
    },
)
