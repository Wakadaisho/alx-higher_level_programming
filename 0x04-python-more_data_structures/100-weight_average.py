#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list or []) == 0):
        return 0
    return sum([i*j for i, j in my_list])/sum([i for _, i in my_list])
