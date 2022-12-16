#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable
found in the header of the response"""
import requests
from sys import argv
if __name__ == "__main__":
    page = requests.get(argv[1])
    print(page.headers.get('X-Request-Id'))
