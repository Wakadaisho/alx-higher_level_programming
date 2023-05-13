#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list and returns a copy

    Args:
        my_list: list of numbers to modify
        idx: index to modify
        element: new value of element modified

    Return:
        modified list copy
    """
    my_list_cpy = my_list[:]
    if (idx < 0 or idx >= len(my_list)):
        return my_list_cpy
    my_list_cpy[idx] = element
    return my_list_cpy
