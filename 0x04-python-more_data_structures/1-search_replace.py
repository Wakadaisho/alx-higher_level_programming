#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (len(my_list or []) == 0):
        return my_list
    cpy = my_list[:]
    for i in range(0, len(cpy)):
        if (cpy[i] == search):
            cpy[i] = replace
    return cpy
