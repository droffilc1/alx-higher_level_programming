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

    def area(self):
        """Public instance method that returns the current square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Property to retrive size

        Property setter to set size
        """

        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #:
        if size is equal to 0, print an empty line
        """
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__size == 0:
                    print()
                else:
                    print("#", end="")
            print()
