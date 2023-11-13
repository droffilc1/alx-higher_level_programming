#!/usr/bin/python3
"""A module for a class Square that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing data."""
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )
