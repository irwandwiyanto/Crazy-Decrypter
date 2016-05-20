#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name                = "crazy_decrypter",
    version             = "0.0.4",
    url                 = 'https://github.com/agusmakmun/Crazy-Decrypter/',
    download_url        = 'https://github.com/agusmakmun/Crazy-Decrypter/tarball/v0.0.3',
    description         = 'Python Crazy Decrypter is real crazy tool to decrypt md5, sha1, sha224, sha256, sha384, and sha512 with Brute Force method.',
    license             = 'MIT',
    author              = 'Agus Makmun (Summon Agus)',
    author_email        = 'ags@dracos-linux.id',
    packages            = find_packages(),
    keywords            = ['Crazy Decrypter', 'Python Crazy Decrypter'],
    scripts             = ['crazy_decrypter'],
)