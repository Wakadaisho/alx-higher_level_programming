#!/usr/bin/python3

def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or len(matrix) == 0):
        raise TypeError("matrix must be a matrix (list of lists) "
                "of integers/floats")
    if (not isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists) "
                "of integers/floats")
    row_size = len(matrix[0])
    for r in matrix:
        if (not isinstance(r, list) or len(r) == 0):
            raise TypeError("matrix must be a matrix (list of lists) "
                    "of integers/floats")
        if (len(r) != row_size):
            raise TypeError("Each row of the matrix must have the same size")
        for c in r:
            if (not isinstance(c, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in r] for r in matrix]

