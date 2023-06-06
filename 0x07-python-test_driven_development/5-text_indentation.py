#!/usr/bin/python3

def text_indentation(text):
    newline = True
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    text = text.strip()
    for c in text:
        if (newline == True and c.isspace()):
            continue
        newline = False
        print(c, end="")
        if (c in ":?."):
            newline = True
            print("\n")
