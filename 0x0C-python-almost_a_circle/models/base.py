#!/usr/bin/python3
"""A module for the Base class."""


import json


class Base:
    """The Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing data."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation

        Args:
            list_dictionaries: A list dictionaries.

        Return: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
