#!/usr/bin/python3
"""This module provides a function for printing a square.

    Example:
    >>> import 4-print_square
    >>> result = 4-print_square.print_square(4)
"""
def print_square(size):
    """This function .

    Args:
        size: The size length of the square.

    Returns:
        Prints a square

    Raises:
        TypeError: If size is not an integer.
                   If size is a float and is less than 0.

        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
