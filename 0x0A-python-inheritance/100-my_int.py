#!/usr/bin/python3

"""
Module 100-my_int
Module that rebels from int
"""


class MyInt(int):
    """int rebel class"""
    def __ne__(self, __value):
        return super().__eq__(__value)

    def __eq__(self, __value):
        return super().__ne__(__value)
