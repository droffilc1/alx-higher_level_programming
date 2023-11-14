#!/usr/bin/python3
"""A module for the Base class."""


import json
import csv


class Base:
    """The Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing data."""
        if id:
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

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes
        already set.
        Args:
            dictionary: Can be thought of as a double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Class method that returns a lsit of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as f:
                json_data = f.read()
        except FileNotFoundError:
            return []

        json_list = cls.from_json_string(json_data)
        new_list = list()
        for dic in json_list:
            obj = cls.create(**dic)
            new_list.append(obj)
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs: The list objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                pass
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    list_dicts = [obj.to_dictionary() for obj in list_objs]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in list_dicts:
                        writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv"""
        data = []

        with open(f"{cls.__name__}.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj = cls.create(
                        width=int(row["width"]),
                        height=int(row["height"]),
                        x=int(row["x"]), y=int(row["y"]),
                        id=int(row["id"])
                    )
                else:
                    obj = cls.create(
                        size=int(row["size"]),
                        x=int(row["x"]), y=int(row["y"]), id=int(row["id"])
                    )
                data.append(obj)
        return data
