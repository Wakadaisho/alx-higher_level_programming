#!/usr/bin/python3

"""
Module 5-save_to_json_file.py
Has function that saves a python object to file
"""


def save_to_json_file(my_obj, filename):
    """
    Saves a python object to file

    Args:
        my_obj: python object
        filename: file to save string to
    """
    import json

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
