# -*- coding: utf-8 -*-

"""
Python Script to download the Chrome Extensions (CRX) file directly from the google chrome web store.
Referred from http://chrome-extension-downloader.com/how-does-it-work.php
"""

import argparse
from urllib.parse import urlparse
import requests
import sys

CRX_URL = "https://clients2.google.com/service/update2/crx?" \
          "response=redirect&prodversion=38.0&x=id%3D~~~~%26installsource%3Dondemand%26uc"
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Referer": "https://chrome.google.com",
}


def download(url, file_path=None):
    chrome_app_id, file_name = parse(chrome_store_url=url)
    if not chrome_app_id:
        raise ValueError("Unable to get Chrome App Id %s" % url)
    download_stream(CRX_URL.replace("~~~~", chrome_app_id), file_path if file_path else file_name)


def download_stream(download_url, file_name):
    try:
        # Download as Stream
        request = requests.get(url=download_url, headers=HEADERS, stream=True)
        redirects = request.history
        if len(redirects) > 0:
            redirect_header = redirects[-1].headers
            if "location" in redirect_header:
                loc = redirect_header["location"]
                splits = urlparse(loc).path.split("/")
                file_name = splits[-1].replace("extension", file_name)
            else:
                file_name += ".crx"
        else:
            file_name += ".crx"

        request_headers = request.headers
        content_length = None
        if "content-length" in request_headers:
            content_length = int(request_headers["content-length"])

        if content_length:
            print("Downloading %s. File Size %s " % (file_name, byte_to_human(content_length)))
        else:
            print("Downloading %s " % file_name)

        chunk_size = 16 * 1024
        dowloaded_bytes = 0
        with open(file_name, 'wb') as fd:
            for chunk in request.iter_content(chunk_size):
                fd.write(chunk)
                dowloaded_bytes += len(chunk)
                sys.stdout.write("\r" + byte_to_human(dowloaded_bytes))
                sys.stdout.flush()
    except Exception as e:
        raise ValueError("Error in downloading %s " % download_url, e)


def parse(chrome_store_url):
    # Try to validate the URL
    parsed_url = urlparse(chrome_store_url)
    if parsed_url.netloc != "chrome.google.com":
        raise ValueError("Not a valid URL %s" % chrome_store_url)
    splits = parsed_url.path.split("/")
    if not (len(splits) == 5 and parsed_url.path.startswith("/webstore/detail/")):
        raise ValueError("Not a valid URL %s" % chrome_store_url)

    return splits[-1], splits[-2]


def byte_to_human(len_in_byte):
    in_kb = len_in_byte / 1024
    in_mb = in_kb / 1024
    in_gb = in_mb / 1024

    if in_kb < 1024:
        return "%.2f KB" % in_kb

    if in_mb < 1024:
        return "%.2f MB" % in_mb

    if in_gb > 1:
        return "%.2f GB" % in_gb


def main():
    # Getting webstore URL from User
    parser = argparse.ArgumentParser(description='Download CRX file from Google Chrome Webstore.')
    parser.add_argument('-u', '--url', help='URL of the chrome store', required=True)
    parser.add_argument('-f', '--file', help='Path to download CRX')
    args = parser.parse_args()

    download(args.url, args.file)


if __name__ == '__main__':
    main()
