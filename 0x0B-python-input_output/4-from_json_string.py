#!/usr/bin/python3
"""A module for a fucntion that returns an object."""


import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        str: The string.

    Return: an object represented by a JSON string.
    """
    return json.loads(my_str)
