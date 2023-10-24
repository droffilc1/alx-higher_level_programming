#!/usr/bin/python3
"""A module of class Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0):
        """Initializes the instance
        Args:
            size: Defines instance attribute
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
