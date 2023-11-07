#!/usr/bin/python3
"""A module for a fucntion that writes an object to a text file."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The object.
        filename: The file to be written to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
