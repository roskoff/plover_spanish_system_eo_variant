#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'plover_spanish_system_eo_variant',
    version = '0.0.3',
    description = 'Spanish System (eo variant) for Plover',
    author = 'Eliseo Ocampos',
    author_email = 'roskoff@gmail.com',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    url = 'https://github.com/roskoff/plover_spanish_system_eo_variant',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords = 'plover plover_plugin',
    setup_requires=['wheel'],
    install_requires = [
        'plover>=4.0.0.dev0',
    ],
    packages = [
        'plover_spanish_system_eo_variant',
    ],
    entry_points = '''

    [plover.system]
    Spanish System (eo variant) = plover_spanish_system_eo_variant.system

    ''',
    include_package_data = True,
    zip_safe = True,
)
