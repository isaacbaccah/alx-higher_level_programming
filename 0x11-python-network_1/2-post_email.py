#!/usr/bin/python3
"""Sends a POST request to the passed URL with an email as a parameter"""
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("{}".format(page.decode('utf8')))
