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
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or\
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
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
