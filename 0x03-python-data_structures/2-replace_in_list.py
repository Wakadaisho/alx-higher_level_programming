#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    """Replace an elemnt in a list with another

    Args:
        my_list: list to modify
        idx: index to modify
        new_element: new item to store

    Return:
        modified list
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list
    my_list[idx] = new_element
    return my_list
