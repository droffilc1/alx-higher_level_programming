#!/usr/bin/python3
"""A module for a fucntion returning a JSON representation."""

import json


def to_json_string(my_obj):
    """Returns a JSON representation of an object(string).

    Args:
        my_obj: string(object)

    Return:
        A JSON representation of an object(string)
    """
    return json.dumps(my_obj)
