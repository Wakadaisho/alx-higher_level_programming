#!/usr/bin/python3

"""
Module 101-add_attribute
Add attribute to objects
"""


def add_attribute(obj, key, value):
    """Add attritube to object if possible

    Args:
        obj: object to modify
        key: name of attribute
        value: value of attribute

    Raises:
        TypeError: if cannot add attribute to object
    """
    if ('__dict__' not in dir(obj)):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
