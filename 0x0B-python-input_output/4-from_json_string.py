#!/usr/bin/python3

"""
Module 4-from_json_string
Has function that converts a JSON string to a python object
"""


def from_json_string(my_str):
    """
    Converts a JSON string to a python object

    Args:
        my_str: JSON string

    Return:
        python object
    """
    import json

    return json.loads(my_str)
