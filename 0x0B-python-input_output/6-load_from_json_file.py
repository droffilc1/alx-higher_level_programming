#!/usr/bin/python3
"""A module for a fucntion that creates an object from a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename: The file name.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
