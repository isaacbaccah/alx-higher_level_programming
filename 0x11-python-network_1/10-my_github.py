#!/usr/bin/python3
"""Script that takes GitHub credentials
and uses GitHub API to display id"""
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    data = response.json()
    print(data.get('id'))
