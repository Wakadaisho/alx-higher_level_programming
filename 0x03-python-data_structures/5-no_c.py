#!/usr/bin/python3
def no_c(my_string):
    """Remove the letter c (uppercase and lowercase) from a string

    Args:
        my_string: string to modify

    Return:
        modified string
    """
    return ''.join([c for c in my_string if c not in 'cC'])
