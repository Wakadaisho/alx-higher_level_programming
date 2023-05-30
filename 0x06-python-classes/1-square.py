#!/usr/bin/python3
"""
Module 1-square
Defines a square class storing the size of its side
"""


class Square:
    """Class representing a square
    """
    def __init__(self, size):
        """Init Square

        Attributes:
            size: length of side of square
        """
        self.__size = size
