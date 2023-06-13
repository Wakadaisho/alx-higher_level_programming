#!/usr/bin/python3

"""
Module 6-load_from_json_file
Has function that reads JSON from a file
"""


def load_from_json_file(filename):
    """
    Reads in a JSON from a file

    Args:
        filename: file to read JSON from

    Return:
        python object
    """
    import json

    obj = None
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
    return obj
