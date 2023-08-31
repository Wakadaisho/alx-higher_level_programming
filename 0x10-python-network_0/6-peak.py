#!/usr/bin/python3
"""Contains function that finds the peak"""


def find_peak(lst):
    """Find the peak in a list of integers

    Args:
        lst (list): list of integers

    Return:
        peak - integer value representing the peak

    """
    if not len(lst or []):
        return None
    left, right = (0, len(lst) - 1)
    mid = left + (right - left) // 2

    if left + 1 == right:
        return max(lst[left], lst[right])

    if mid == 0:
        return lst[mid]

    if (lst[left] > lst[left + 1]):
        return lst[left]

    if (lst[right] > lst[right - 1]):
        return lst[right]

    if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
        return lst[mid]

    if lst[mid] > lst[mid - 1]:
        return find_peak(lst[mid + 1:right + 1])
    elif lst[mid] > lst[mid + 1]:
        return find_peak(lst[left:mid])
    else:
        return find_peak(lst[mid:right + 1])
