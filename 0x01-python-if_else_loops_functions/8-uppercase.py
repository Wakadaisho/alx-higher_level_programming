#!/usr/bin/python3
def uppercase(s):
    for c in s:
        i = ord(c)
        print(f"{(i >= 97 and i <= 122) and chr(i-ord(' ')) or c}", end='')
    print()
