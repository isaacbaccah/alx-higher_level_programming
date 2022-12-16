#!/usr/bin/python3
"""Sends POST request to url with the letter as a parameter"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        param = ""
    else:
        param = argv[1]
    letter_param = {"q": param}
    page = requests.post("http://0.0.0.0:5000/search_user", letter_param)
    try:
        page_to_json = page.json()
        if len(page_to_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(page_to_json.get('id'),
                                   page_to_json.get('name')))
    except ValueError:
        print("Not a valid JSON")
