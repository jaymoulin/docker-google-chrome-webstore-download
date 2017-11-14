#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='chrome_webstore_download',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Jay MOULIN",
    author_email="jaymoulin@gmail.com",
    description="Google Chrome Webstore downloader",
    long_description=open('README.rst').read(),
    install_requires=["gmusicapi"],
    include_package_data=True,
    url='http://github.com/jaymoulin/docker-google-chrome-webstore-download/',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: File Sharing",
        "Topic :: Artistic Software",
        "Topic :: Internet :: File Transfer Protocol (FTP)",
        "Topic :: Home Automation",
        "Topic :: Internet",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    entry_points={
        'console_scripts': [
            'chrome-webstore-download = chrome_webstore_download.download:main',
        ],
    },
    license="MIT",
)
