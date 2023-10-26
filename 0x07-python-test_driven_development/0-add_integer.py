#!/usr/bin/python3
"""module: 0-add_integer.py"""


def add_integer(a, b=98):
    """Adds 2 integers
    Float arguments are typecasted to integers before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
