#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join([i != n and c or '' for i, c in enumerate(str)])
