#!/usr/bin/python3
"""A MyInt class module."""


class MyInt(int):
    """MyInt class."""
    def __new__(cls, num):
        """Create and return a new instance of the class."""
        return super().__new__(cls, num)

    def __init__(self, num):
        """Initializing data."""
        self.num = num

    def __eq__(self, num2):
        """Override equality operator."""
        return self.num != num2

    def __ne__(self, num2):
        """Override inequality operator."""
        return self.num == num2
