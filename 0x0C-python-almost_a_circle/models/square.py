#!/usr/bin/python3
"""A module for a class Square that inherits from Rectangle."""


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
        return self.width

    @size.setter
    def size(self, value):
        # width npt __width
        # because you're calling width setter to set it to value
        self.width = value
        self.height = value

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

    def to_dictionary(self):
        """Returns the dictionary represenation of a Rectangle"""
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.size
        }
