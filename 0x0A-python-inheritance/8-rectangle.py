#!/usr/bin/python3

"""
Module 8-rectangle
Define a rectangle
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Define a rectangle class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
