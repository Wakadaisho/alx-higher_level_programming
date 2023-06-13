#!/usr/bin/python3

"""
Module 10-student

Contains a class defining a Student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Represent a student in JSON format

        Args:
            attrs: filter keys

        Return:
            dictionary representation of object
        """
        attrs = attrs or []
        data = self.__dict__.copy()
        if (len(attrs) == 0):
            return data
        return dict(filter(lambda k: k[0] in attrs, data.items()))
