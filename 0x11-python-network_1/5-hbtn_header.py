#!/usr/bin/python3
"""Fetch a webpage using requests and display a header"""

import requests
from sys import argv

if __name__ == "__main__":
    data = requests.get(argv[1])
    print(data.headers.get('X-Request-Id'))
