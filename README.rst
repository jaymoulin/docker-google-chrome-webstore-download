.. image:: https://raw.githubusercontent.com/jaymoulin/docker-google-chrome-webstore-download/master/logo.png
    :alt: logo
    :target: http://github.com/jaymoulin/docker-google-chrome-webstore-download

=================================================
Google Chrome Webstore Downloader - Python Module
=================================================

.. image:: https://img.shields.io/github/release/jaymoulin/docker-google-chrome-webstore-download.svg
    :alt: latest release
    :target: http://github.com/jaymoulin/docker-google-chrome-webstore-download/releases
.. image:: https://img.shields.io/pypi/v/chrome_webstore_download.svg
    :alt: PyPI version
    :target: https://pypi.org/project/chrome_webstore_download/
.. image:: https://img.shields.io/docker/pulls/jaymoulin/google-chrome-webstore-download.svg
    :target: https://hub.docker.com/r/jaymoulin/google-chrome-webstore-download/
.. image:: https://img.shields.io/docker/stars/jaymoulin/google-chrome-webstore-download.svg
    :target: https://hub.docker.com/r/jaymoulin/google-chrome-webstore-download/
.. image:: https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ppl.png
    :alt: PayPal donation
    :target: https://www.paypal.me/jaymoulin
.. image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
    :alt: Buy me a coffee
    :target: https://www.buymeacoffee.com/3Yu8ajd7W
.. image:: https://badgen.net/badge/become/a%20patron/F96854
    :alt: Become a Patron
    :target: https://patreon.com/jaymoulin

This program will download Google Chrome Webstore extension CRX files to you computer

This work is based upon `arulrajnet's work <https://gist.githubusercontent.com/arulrajnet/2424bc1ffc40324f3786/raw/dc6e7e5f0edfe05e5eae0a65724c654cba2b9d70/ChromeAppDownloader.py>`_.

Installation
------------

.. code::

    pip3 install chrome_webstore_download


Once installed, You will be able to download CRX files from webstore via the `chrome-webstore-download` command

.. code::

    usage: chrome-webstore-download [-h] -u URL [-f FILE]

    Download CRX file from Google Chrome Webstore.

    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     URL of the chrome store
      -f FILE, --file FILE  Path to download CRX

Example
~~~~~~~

.. code::

    chrome-webstore-download -u https://chrome.google.com/webstore/detail/bandcamp-downloader/nmoobgpmablfmgchfjnhkbloaobiogeh

============
Docker Usage
============

.. code::

    docker run --rm -ti -v `pwd`:/root jaymoulin/google-chrome-webstore-download <option>

.. code::

    usage: jaymoulin/google-chrome-webstore-download [-h] -u URL [-f FILE]

    Download CRX file from Google Chrome Webstore.

    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     URL of the chrome store
      -f FILE, --file FILE  Path to download CRX

Example
-------

.. code::

    docker run --rm -ti -v `pwd`:/root jaymoulin/google-chrome-webstore-download -u https://chrome.google.com/webstore/detail/bandcamp-downloader/nmoobgpmablfmgchfjnhkbloaobiogeh

=====
About
=====

Requirements
------------

Google Chrome Webstore Downloader works with Python 3 or above.

Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on GitHub

Author
------

Jay MOULIN jaymoulin@gmail.com See also the list of contributors which participated in this program.

License
-------

Google Chrome Webstore Downloader is licensed under the MIT License
