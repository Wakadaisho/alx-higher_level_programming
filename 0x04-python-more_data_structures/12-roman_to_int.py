#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
    if (not isinstance(roman_string, str) or len(roman_string) == 0):
        return 0
    integer = 0
    last_value = 0
    for c in roman_string[::-1]:
        if (numerals[c] >= last_value):
            integer += numerals[c]
            last_value = numerals[c]
        else:
            integer -= numerals[c]
    return integer
