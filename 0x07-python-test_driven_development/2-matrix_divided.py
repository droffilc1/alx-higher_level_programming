#!/usr/bin/python3
"""This module provides a function for dividing a matrix by a divisor.

    Example:
    >>> import 2-matrix_divided
    >>> result = 2-matrix_divided.matrix_divided(matrix, 3)
"""
def matrix_divided(matrix, div):
    """This function divides all elements of a matrix.

    Args:
        matrix: A list lof lists of integers.
        div: The divisor.

    Returns:
        A new matrix divided by the divisor

    Raises:
        TypeError: If matrix is not a list of lists of integers.

        TypeError: If row of the matrix is not of the same size.

        TypeError: if div is not a number(integer or float).

        ZeroDivisionError: if div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
