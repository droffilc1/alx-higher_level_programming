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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
