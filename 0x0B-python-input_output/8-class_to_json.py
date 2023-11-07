#!/usr/bin/python3
"""A module for a function that returns a dictionary description with
simple data structure.
"""


def class_to_json(obj):
    """Returns a dictionary description with simple data structure."""
    return obj.__dict__
