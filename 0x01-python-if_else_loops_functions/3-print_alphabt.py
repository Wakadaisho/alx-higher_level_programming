#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(c) not in 'eq' and chr(c) or ''), end='')
