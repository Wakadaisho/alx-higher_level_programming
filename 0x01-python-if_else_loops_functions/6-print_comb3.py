#!/usr/bin/python3
for i in range(0, 100):
    if not (i // 10 >= i % 10):
        print(f"{i:02}{i != 89 and ', ' or chr(10)}", end='')
