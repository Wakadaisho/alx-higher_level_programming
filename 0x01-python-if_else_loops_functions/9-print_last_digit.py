#!/usr/bin/python3
def print_last_digit(n):
    n = n < 0 and -n % 10 or n % 10
    print(n, end='')
    return n
