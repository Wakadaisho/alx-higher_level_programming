#!/usr/bin/python3

"""
Module 0-lookup
Find the available attributes and methods of an object
"""


def lookup(obj):
    """Return the available attributes and methods of an object

    Args:
        obj: object to check

    Return:
        a list object
    """
    return dir(obj)
