#!/usr/bin/python3
def max_integer(my_list=[]):
    """Return the largest integer in a list

    Args:
        List of integers

    Return:
        Largest integer
    """
    max = None
    if (len(my_list)):
        max = my_list[0]
        for i in my_list:
            max = i > max and i or max
        return max
    return max
