#!/usr/bin/python3
"""A module for a Pascal's triangle function."""


def pascal_triangle(n):
    """Creates the Pascal's triangle.

    Args:
        n: size of the rectangle.

    Return:
        A list of lists of integers representing the Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return []

    for i in range(n):
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1, len(row) - 1):
            row_above = triangle[i - 1]
            row[j] = row_above[j] + row_above[j - 1]
        triangle.append(row)
    return triangle
