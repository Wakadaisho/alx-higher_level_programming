#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Filter a list to numbers divisible by 2

    Args:
        my_list: list of numbers

    Return:
        list of even number
    """
    return [b % 2 == 0 for b in my_list]
