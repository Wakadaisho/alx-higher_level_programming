#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cpy = my_list[:]
    if (idx < 0):
        return my_list_cpy
    if (idx >= len(my_list)):
        return None
    my_list_cpy[idx] = element
    return my_list_cpy
