#!/usr/bin/python3

"""
Module 100-matrix_mul
Find the dot product of two matrices
Return the new matrix
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a: matrix 1
        m_b: matrix 2

    Raises:
        TypeError: if matrices are not list of lists of numbers
                    if the matrices don't have the same length rows
        ValueError: if matrices are empty lists
                    if matrices cannot be multiplied
    """
    # Check for list of lists
    if (not isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if (not isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    for r in m_a:
        if (not isinstance(r, list)):
            raise TypeError("m_a must be a list of lists")
    for r in m_b:
        if (not isinstance(r, list)):
            raise TypeError("m_b must be a list of lists")

    # Check if empty
    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    # Check if elements are all integers and floats
    for r in m_a:
        for c in r:
            if (not isinstance(c, (int, float))):
                raise TypeError("m_a should contain only integers or floats")
    for r in m_b:
        for c in r:
            if (not isinstance(c, (int, float))):
                raise TypeError("m_b should contain only integers or floats")

    # Check if square
    row_size = len(m_a[0])
    for r in m_a:
        if (len(r) != row_size):
            raise TypeError("each row of m_a must be of the same size")
    row_size = len(m_b[0])
    for r in m_b:
        if (len(r) != row_size):
            raise TypeError("each row of m_b must be of the same size")

    # Check if can be multiplied
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c
