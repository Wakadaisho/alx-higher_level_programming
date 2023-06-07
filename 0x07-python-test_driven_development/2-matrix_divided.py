#!/usr/bin/python3

"""
Module 2-matrix_divided
Divide a matrix's elements by a number
Return a matrix with values in 2 decimal places
"""


def matrix_divided(matrix, div):
    """Divide a matrix (scale)

    Args:
        matrix: 2D list representing a matrix
        div: float or div to divide matrix elements by

    Raises:
        TypeError: if matrix is not a list of lists or
                    an element is not a number
        ZeroDivisionError: if div is 0
    """
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
