#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle class storing the size of its sides
"""


class Rectangle:
    """Class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        """Init Rectangle

        Attributes:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter

        Args:
            value: width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter

        Args:
            value: height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value