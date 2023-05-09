#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number < 0 and -(-number % 10) or number % 10

print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")

if last_digit == 0:
    print(f"0")
elif last_digit < 6:
    print(f"less than 6 and not 0")
else:
    print(f"greater than 5")
