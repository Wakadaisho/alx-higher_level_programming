#!/usr/bin/python3

"""
Module 101-locked_class
Create a locked class using slots to prevent
the dynamic creation of attributes.
"""


class LockedClass:
    """Class with only the 'first_name' attribute allowed"""
    __slots__ = ["first_name"]
