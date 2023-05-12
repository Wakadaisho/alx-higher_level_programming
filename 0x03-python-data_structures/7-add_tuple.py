#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0, 0]
    if (len(tuple_a) == 0):
        pass
    elif (len(tuple_a) == 1):
        sum[0] += tuple_a[0]
    else:
        sum[0] += tuple_a[0]
        sum[1] += tuple_a[1]

    if (len(tuple_b) == 0):
        pass
    elif (len(tuple_b) == 1):
        sum[0] += tuple_b[0]
    else:
        sum[0] += tuple_b[0]
        sum[1] += tuple_b[1]
    return tuple(sum)
