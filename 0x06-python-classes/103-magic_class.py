#!/usr/bin/python3
import math

"""
Module 103-magic_class.py
Defines a circle class
Takes in a radius on initialization
Defines methods for finding area and perimeter of the circle
"""


class MagicClass:
    """Class representing a magic structure, likely a circle"""
    def __init__(self, radius):
        """Init MagicClass

        Args:
            radius (number): int or float for radius

        Raises:
            TypeError: if radius is not a number
        """
        if (not (isinstance(radius, int) or isinstance(radius, float))):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Find area of a circle

        Args:
            radius (number): radius of the circle

        Returns:
            number: area of a circle
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """Find perimeter of a circle

        Args:
            radius (number): radius of the circle

        Returns:
            number: perimeter of a circle
        """
        return 2 * math.pi * self.__radius
