#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list in reverse

    Args:
        my_list: list of numbers

    Return:
        None
    """
    my_list = my_list or []
    for i in my_list[::-1]:
        print("{:d}".format(i))
