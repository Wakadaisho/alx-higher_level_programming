#!/usr/bin/python3
"""
Reqeust a url and display body content
Handle http errors
"""

from urllib import error, request
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode())
    except error.HTTPError as e:
        print("Error code:", e.code)
