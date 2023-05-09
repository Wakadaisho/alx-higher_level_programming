#!/usr/bin/python3
s = ''.join([chr(c + (~c & 1) * 32) for c in range(90, 64, -1)])
print("{}".format(s), end='')
