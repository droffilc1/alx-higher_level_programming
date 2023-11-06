#!/usr/bin/python3
"""A module for a BaseGeometry class."""


class BaseGeometry:
    """A simple BaseGeometry class.

    Raises:
        Exception: area() is not implemented.
    """
    def area(self):
        """Calculates the area."""
        raise Exception("area() is not implemented")
