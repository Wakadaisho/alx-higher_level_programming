#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i*i for i in r] for r in matrix or []]
