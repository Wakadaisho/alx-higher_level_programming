#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print the numbers in a list

    Args:
        my_list: list of numbers

    Return:
        None
    """
    for i in my_list:
        print("{:d}".format(i))
