#!/usr/bin/python3

"""
Module 100-lazy_matrix_mul
Find the dot product of two matrices
Return the new matrix
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Find dot product of two matrices using numpy

    Args:
        m_a: matrix 1
        m_b: matrix 2
    """
    return np.dot(m_a, m_b)
