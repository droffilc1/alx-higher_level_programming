#!/usr/bin/python3
"""A class Student module."""


class Student:
    """A Student class."""
    def __init__(self, first_name, last_name, age):
        """Initializing data."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary represenation of a Student instance."""
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        return self.__dict__.update(json)
