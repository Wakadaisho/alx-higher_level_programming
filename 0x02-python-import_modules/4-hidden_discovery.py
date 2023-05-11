#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    symbols = [s for s in dir(hidden_4) if not s.startswith('__')]
    symbols.sort()
    for s in symbols:
        print(s)
