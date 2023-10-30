#!/usr/bin/python3
"""A module for a rectangle class."""


class Rectangle:
    """Defines a rectangle class."""
    def __init__(self, width=0, height=0):
        """Initializing data.

        Args:
            width: Defines width of the rectangle.
            height: Defines height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines the width of the rectangle.

        Defines setter for width of the rectangle.

        Raises:
              TypeError: if width is not an integer.
              ValueError: if width is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines the height of the rectangle.

        Defines setter for height of the rectangle.

        Raises:
              TypeError: if height is not an integer.
              ValueError: if height is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        """Prints a rectangle of an object"""
        if self.width == 0 or self.height == 0:
            return ""
        my_print = ""
        for i in range(self.height):
            for j in range(self.width):
                my_print += "#"
            if i != self.height - 1:
                my_print += "\n"
        return my_print
