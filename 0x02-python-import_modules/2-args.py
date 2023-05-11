#!/usr/bin/env python3

from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if (argc):
        print(f"{argc:d} argument{argc == 1 and ':' or 's:'}")
        for i in range(1, argc + 1):
            print(f"{i:d}: {argv[i]}")
    else:
        print("0 arguments.")
