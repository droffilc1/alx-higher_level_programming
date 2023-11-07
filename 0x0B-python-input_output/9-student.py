#!/usr/bin/python3
"""A class Student module."""


class Student:
    """A Student class."""
    def __init__(self, first_name, last_name, age):
        """Initializing data."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary represenation of a Student instance."""
        return self.__dict__
