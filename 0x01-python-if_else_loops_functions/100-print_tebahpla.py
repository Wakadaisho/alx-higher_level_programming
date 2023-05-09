#!/usr/bin/python3
print(''.join([chr(c + (~c & 1) * 32) for c in range(90, 64, -1)]), end='')
