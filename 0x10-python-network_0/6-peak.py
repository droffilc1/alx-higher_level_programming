#!/usr/bin/python3
"""find peak in a list of unsorted integers."""


def find_peak(lst):
    """finds peak in a list of unsorted integers."""
    start, end = 0, len(lst) - 1
    if lst == []:
        return None

    while start < end:
        mid = start + (end - start) // 2

        # check if it's a peak
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]

        if lst[start] > lst[mid] and lst[start] > lst[end]:
            return lst[start]

        if lst[mid - 1] > lst[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return lst[start]
