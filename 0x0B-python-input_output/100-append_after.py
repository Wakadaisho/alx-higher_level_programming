#!/usr/bin/python3

"""
Module 100-append_after
Contains a function that adds lines to files
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line into a file after a text match is found

    Args:
        filename: file to be processed
        search_string: line in file to search
        new_string: string to insert into the file
    """
    lines = []
    output = []
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            output.append(line)
            if (line.count(search_string)):
                output.append(new_string)
        f.seek(0)
        f.truncate(0)
        f.writelines(output)
