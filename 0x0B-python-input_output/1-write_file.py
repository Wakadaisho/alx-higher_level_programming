#!/usr/bin/python3

"""
Module 1-write_file
Write out strings to a text file in UTF8
"""


def write_file(filename="", text=""):
    """Write out text to a file

    Args:
        filename: name of file to write
        text: text to write in file

    Return:
        number of characters written
    """
    chars = None
    with open(filename, "wt", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
