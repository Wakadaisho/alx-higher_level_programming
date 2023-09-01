#!/usr/bin/python3
"""Fetch a webpage and display the value of a header"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as res:
        print(res.getheader('X-Request-Id'))
