#!/usr/bin/python3

"""
Module 10-square
Define a square
"""


class Square(__import__('9-rectangle').Rectangle):
    """Define a sqaure class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of a square"""
        return self.__size * self.__size
