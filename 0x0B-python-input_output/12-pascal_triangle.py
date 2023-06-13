#!/usr/bin/python3

"""
Module 12-pascal_triangle
Create Pascals triangle
"""


def pascal_triangle(n):
    """Represent Pascal's triangle using a list of ints

    Args:
        n: numeber of layers in the triangle

    Return:
        list of lists of rows of triangle
    """

    triangle = []

    if (n <= 0):
        return triangle

    def fact(n):
        """Find the factorial of a number

        Args:
            n (int): number >= 0

        Return:
            integer
        """
        if (n == 0):
            return 1
        return n * fact(n - 1)

    def comb(n, c):
        """Find the combinatorial n!/((n-c)!(c!))

        Args:
            n: permutation space
            c: combinatorial

        Return:
            integer
        """
        return fact(n) // (fact(n - c) * fact(c))

    for i in range(0, n):
        row = []
        for j in range(0, i):
            row.append(comb(i, j))
        row.append(1)
        triangle.append(row)

    return triangle
