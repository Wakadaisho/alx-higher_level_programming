#!/usr/bin/python3

"""
Module 7-base_geometry
Define a geometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Return area

        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name: a string
            value: integer greater than 0

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if (type(value).__name__ != int.__name__):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
