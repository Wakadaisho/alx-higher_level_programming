#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix

    Args:
        matrix: 2D list

    Return:
        None
    """
    if (matrix != [[]] and matrix is not None):
        for r in matrix:
            for c in r[:-1]:
                print("{:d}".format(c), end=' ')
            print("{:d}".format(r[-1]))
    else:
        print()
