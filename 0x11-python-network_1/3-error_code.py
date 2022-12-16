#!/usr/bin/python3
"""Sends a request to the URL and displays the body
of the response decoded in utf8"""
import urllib.request
import urllib.error
from sys import argv
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            page = response.read()
            print("{}".format(page.decode('utf8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
