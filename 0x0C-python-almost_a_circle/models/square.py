#!/usr/bin/python3
"""A module for a class Square that inherits from Rectangle."""


from re import X
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing data."""
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Property to retrieve size.
        Property setter to set size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args[:4]):
                setattr(self, attrs[i], value)

        for key, value in kwargs.items():
            setattr(self, key, value)
