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

    @classmethod
    def save_to_file(cls, list_objects):
        """Class method that writes the JSON string representation
        of list_objects to file.

        Args:
            list_objects: A list of instances who inherits from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objects is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objects]
                json_str = Base.to_json_string(list_dict)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the lit of the JSON string
        representation json_string.

        Args:
            json_string: A string representing a list of dictionaries.

        Return: The list represented by json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)
