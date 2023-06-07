#!/usr/bin/python3

"""
Module 5-text_indentation

"""


def text_indentation(text):
    """Split a string to lines ba sed on ':?.' symbols

    Args:
        text: text to split

    Raises:
        TypeError: if text is not a string
    """
    newline = True
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    text = text.strip()
    for c in text:
        if (newline and c.isspace()):
            continue
        newline = False
        print(c, end="")
        if (c in ":?."):
            newline = True
            print("\n")
