#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [i == search and replace or i for i in my_list or []]
