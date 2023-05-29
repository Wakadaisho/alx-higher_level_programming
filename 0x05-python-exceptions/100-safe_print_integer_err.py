#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    result = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print(f"Exception: {err}", file=sys.stderr)
        result = False
    return result
