#!/usr/bin/python3

"""
Module 0-add_integer
Add two integers, or floats casted to integers
Return the sum as an integer
"""


def add_integer(a, b=98):
    """
    Return the sum of two numbers as an integer
    """
    if (not (isinstance(a, (int, float)))):
        raise TypeError("a must be an integer")
    if (not (isinstance(b, (int, float)))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
