#!/usr/bin/python3

"""
Module 9-student

Contains a class defining a Student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Represent a student in JSON format"""
        return self.__dict__
