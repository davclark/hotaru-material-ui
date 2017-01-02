# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

name = 'hotaru_web'
description = (
    'A morepath web interface for blinky lights'
)
version = '0.0.0'


setup(
    name=name,
    version=version,
    description=description,
    author='Dav Clark',
    author_email='davclark@gmail.com',
    packages=find_packages(),
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    # This doesn't work, so using python 2 for now
    # dependency_links=['https://github.com/ManiacalLabs/BiblioPixel/tarball/dev#egg=BiblioPixel-3.dev'],
    install_requires=[
        'morepath',
	'BiblioPixel',
        'spidev',
    ],
    extras_require=dict(
        test=[
            'pytest',
            'webtest',
        ],
    ),
    entry_points=dict(
        console_scripts=[
            'run-app = hotaru_web.__main__:run',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
