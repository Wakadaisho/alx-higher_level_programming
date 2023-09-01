#!/usr/bin/python3
"""Fetch a webpage using requests"""

import requests

if __name__ == "__main__":
    data = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))
