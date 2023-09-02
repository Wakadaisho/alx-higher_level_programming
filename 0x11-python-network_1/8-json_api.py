#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {'q': len(argv) > 1 and argv[1] or ""}

    res = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        res.raise_for_status()
        json = res.json()
        if len(json):
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    except requests.exceptions.HTTPError:
        print("No result")
