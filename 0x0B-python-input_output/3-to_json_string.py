#!/usr/bin/python3

"""
Module 3-to_json_string
Has function that converts an object to a JSON string
"""


def to_json_string(my_obj):
    """
    Dumps a python object as a JSON string

    Args:
        my_obj: python object

    Return:
        string in json format
    """
    import json

    return json.dumps(my_obj)
