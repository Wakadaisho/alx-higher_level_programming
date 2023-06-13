#!/usr/bin/python3

"""
Module 8-class_to_json.py

Contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Serialize an object to JSON

    Args:
        obj: class object instance

    Return:
        object dict
    """
    return obj.__dict__
