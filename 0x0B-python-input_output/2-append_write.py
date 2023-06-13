#!/usr/bin/python3

"""
Module 2-append_write
Append strings to a text file in UTF8
"""


def append_write(filename="", text=""):
    """Write out text to a file, appending

    Args:
        filename: name of file to write
        text: text to write in file

    Return:
        number of characters written
    """
    chars = None
    with open(filename, "a", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
