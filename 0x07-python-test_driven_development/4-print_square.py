#!/usr/bin/python3

"""
Module 4-print_square
Print a square ASCII art based on a defined size
Returns nothing
"""


def print_square(size):
    """Print a sqaure using a symbol

    Args:
        size: dimensions of the sqaure

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is negative
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)
