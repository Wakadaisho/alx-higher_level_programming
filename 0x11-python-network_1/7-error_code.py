#!/usr/bin/python3
"""
Reqeust a url using requests, display body content
Handle http errors
"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])

    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
