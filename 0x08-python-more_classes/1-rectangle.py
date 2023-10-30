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
        self.__width = width
        self.__height = height

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

        if self.__width < 0:
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

        if self.__height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
