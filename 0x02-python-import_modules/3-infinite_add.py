#!/usr/bin/python3

from sys import argv


def sub_str(a='0', b='0'):
    """Find difference of two strings of numbers,
        one negative, one positive

    Args:
        a: first string of numbers
        b: second string of numbers

    Returns:
        difference between a and b as a string
    """
    diff = ''
    brw = 0     # borrow value
    pos = a[0] == '-' and b or a
    neg = pos == a and b[1:] or a[1:]
    delta = len(neg) - len(pos)
    if (delta > 0):
        a = neg
        b = pos
    elif (delta < 0):
        a = pos
        b = neg
    else:
        if (neg > pos):
            a = neg
            b = pos
            delta = 1
        else:
            a = pos
            b = neg
            delta = -1
    a = a[::-1]     # larger of the two numbers
    b = b[::-1]     # smaller of the two numbers
    b += '0' * (len(a)-len(b))
    for i in range(0, len(a)):
        diff += str((int(a[i]) - brw) +
                    ((int(b[i]) > (int(a[i]) - brw)) and 10) - int(b[i]))
        brw = int(b[i]) > (int(a[i]) - brw)
    diff = diff.rstrip('0')
    if (len(diff) == 0):
        return '0'
    return f"{delta > 0 and '-' or ''}{diff[::-1]}"


def add_str(a='0', b='0'):
    """Find sum of two strings of natural numbers

    Args:
        a: first string of numbers
        b: second string of numbers

    Returns:
        a + b as a string
    """
    sum = ''
    carry = 0
    tmp = 0
    delta = len(a) - len(b)
    a = a[::-1]
    b = b[::-1]
    if (delta > 0):
        b += '0' * delta
    else:
        a += '0' * -delta
    for i in range(0, len(a)):
        tmp = int(a[i]) + int(b[i]) + carry
        carry = 0
        if (tmp > 9):
            carry = 1
            tmp %= 10
        sum += str(tmp)
    sum += '1' * carry
    return sum[::-1]


if __name__ == "__main__":
    positive_sum = '0'  # store positive sums
    negative_sum = '0'  # store negative sums
    for n in argv[1:]:
        if (n[0] == '-'):
            negative_sum = add_str(negative_sum, n[1:])
        else:
            positive_sum = add_str(positive_sum, n)
    print(sub_str(positive_sum, f"-{negative_sum}"))
