#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]] or matrix == None):
        print()
        return;
    for r in matrix:
        for c in r[:-1]:
            print("{:d}".format(c), end=' ')
        print("{:d}".format(r[-1]))
