#!/usr/bin/python3
def uppercase(s):
    for c in s:
        i = ord(c)
        print("{}".format((i >= 97 and i <= 122) and chr(i - 32) or c), end='')
    print()
