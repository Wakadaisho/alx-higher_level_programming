#!/usr/bin/python3
"""
Module 3-square
Defines a square class storing the size of its side
Checks for the size to be valid
Can calculate area
"""


class Square:
    """Class representing a square
    """
    def __init__(self, size=0):
        """Init Square

        Attributes:
            size: length of side of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find area of square

        Args:
            size (int): length of side of square

        Returns:
            int: area of square
        """
        return self.__size * self.__size
