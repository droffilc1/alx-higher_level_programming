#!/usr/bin/python3
"""A module of class Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance
        Args:
            size: Defines instance attribute
            position: Defines instance attribute
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

        if isinstance(position, tuple):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Property to retrieve size

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

    @property
    def position(self):
        """Property to retrieve position
        Property setter to set position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Public instance method that prints in stdout
        the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for m in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
