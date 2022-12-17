#!/usr/bin/python3
""" Sends a POST request to Github repo API """
import requests
from sys import argv


if __name__ == "__main__":
    rep_name = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + rep_name + '/commits'
    req = requests.get(url)
    user_json = req.json()
    counter = 0
    for d in user_json:
        if (counter < 10):
            if (type(d) is dict):
                print("{}: {}".format(d['sha'],
                                      d['commit'].get('author').get('name')))
            counter += 1
        else:
            break
