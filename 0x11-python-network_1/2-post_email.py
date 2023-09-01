#!/usr/bin/python3
"""POST data and output the response"""

from urllib import parse, request
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    data = parse.urlencode(data).encode('ascii')
    req = request.Request(argv[1], data)

    with request.urlopen(req) as res:
        print(res.read().decode())
