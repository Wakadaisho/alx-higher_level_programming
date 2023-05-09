#!/usr/bin/python3
for i in range(0, 100):
    print(f"{i:02}{i != 99 and ', ' or chr(10)}", end='')
