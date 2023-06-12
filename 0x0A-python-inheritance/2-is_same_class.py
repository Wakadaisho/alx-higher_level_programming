#!/usr/bin/python3

"""
Module 2-is_same_class
Check if an object is an instance of a certain class
"""


def is_same_class(obj, a_class):
    """
    Check whether an object is an instance of a class

    Args:
        obj: the object to check
        a_class: the class to compare identitiy to

    Return:
        True if instance, False otherwise
    """
    return type(obj).__name__ == a_class.__name__
