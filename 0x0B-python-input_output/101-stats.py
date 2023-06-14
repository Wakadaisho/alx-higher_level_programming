#!/usr/bin/python3

"""
Module 101-stats
Reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    Total file size: File size: <total size>
    where size is the sum of all previous entries
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear, don’t print anything
        format: <status code>: <number>
        status codes should be printed in ascending order
"""


def print_block(size, codes):
    print("File size: {:d}".format(size))
    for k, v in sorted(codes.items()):
        if (v):
            print("{:s}: {:d}".format(k, v))


if __name__ == "__main__":
    import sys

    codes = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    size = 0
    lines = 0
    try:
        for line in sys.stdin:
            cols = line.strip().split(" ")
            if (len(cols) == 1):
                continue
            size += int(cols[-1])
            if (cols[-2] in codes):
                codes[cols[-2]] += 1
            lines += 1
            if (lines % 10 == 0):
                print_block(size, codes)
    except KeyboardInterrupt:
        print_block(size, codes)
    print_block(size, codes)
