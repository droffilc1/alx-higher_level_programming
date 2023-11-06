#!/usr/bin/python3
"""A module for a BaseGeometry class."""


class BaseGeometry:
    """A simple BaseGeometry class.

    Raises:
        Exception: area() is not implemented.
        TypeError: <name> must be an integer.
        ValueError: <name> must be greater than 0.
    """
    def area(self):
        """Calculates the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Inherits from Base class."""
    def __init__(self, width, height):
        """Initializing data."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
