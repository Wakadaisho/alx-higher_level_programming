#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an element from a list

    Args:
        my_list: list of elements
        idx: index of item to delete

    Return:
        list with item deleted
    """
    if (idx < len(my_list) and idx >= 0):
        del my_list[idx]
    return my_list
