# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
sys.path.insert(0, 'src')
import {{ project_name }}

requires = [
    'django',
]

setup(
    name='{{ project_name }}',
    version={{ project_name }}.__version__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.manage:main',
        ]
    },
)
