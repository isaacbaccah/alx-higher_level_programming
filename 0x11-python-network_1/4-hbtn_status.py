#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import requests
if __name__ == "__main__":
    page = requests.get('https://intranet.hbtn.io/status')
    page_content = page.text
    print("Body response:")
    print("\t- type: {}".format(type(page_content)))
    print("\t- content: {}".format(page_content))
