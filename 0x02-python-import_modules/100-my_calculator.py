#!/usr/bin/env python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    OPS = {'+': add, '-': sub, '*': mul, '/': div}

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if (sys.argv[2] not in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    print(f"{a} {op} {b} = {OPS[op](a, b)}")
