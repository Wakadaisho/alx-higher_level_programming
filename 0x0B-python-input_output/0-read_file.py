#!/usr/bin/python3

"""
Module 0-read_file
Read a file and print to stdout
"""


def read_file(filename=""):
    """Read and write out file to stdout

    Args:
        filename: name of file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
