#!/usr/bin/python3
def element_at(my_list, idx):
    """Return element at an index in list

    Args:
        my_list: list of elements
        idx: index of elemnt to return

    Return:
        element in list
    """
    if (idx < 0 or idx >= len(my_list)):
        return None
    return my_list[idx]
