#!/usr/bin/python3

"""
Module 3-is_kind_of_class
Check whether an object is an instance of or an instance of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Check whether an object is an instance of
    or an instance of an inherited class

    Args:
        obj: the object to check
        a_class: the class to check for

    Return:
        True if instance, False otherwise
    """
    return isinstance(obj, a_class)
