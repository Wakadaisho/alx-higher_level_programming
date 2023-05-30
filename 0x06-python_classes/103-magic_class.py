#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius):
        if (not (isinstance(radius, int) or isinstance(radius, float))):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
