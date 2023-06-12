#!/usr/bin/python3

"""
Module 1-my_list
Defines a class inheriting from list
"""


class MyList(list):
    """Class MyList
    Inherites from list
    """

    def print_sorted(self):
        """Print out integer list in ascending order"""
        lst_copy = self.copy()
        lst_copy.sort()
        print(lst_copy)
