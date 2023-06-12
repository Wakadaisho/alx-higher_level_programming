#!/usr/bin/python3

"""
Module 3-inherits_from
Check whether an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Check whether an object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: the object to check
        a_class: the class to check for

    Return:
        True if instance, False otherwise
    """
    return type(obj).__name__ != a_class.__name__ and isinstance(obj, a_class)
