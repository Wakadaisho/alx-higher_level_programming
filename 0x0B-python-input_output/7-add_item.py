#!/usr/bin/python3

"""
Module 7-add_item
Save command line arguments to a file
"""


if __name__ == "__main__":
    save_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json_file = __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"

    import sys

    lst = []

    try:
        lst = load_json_file(filename)
    except FileNotFoundError:
        pass
    finally:
        save_json_file(lst + sys.argv[1:], filename)
