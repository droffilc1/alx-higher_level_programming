#!/usr/bin/python3
"""A module for a function that checks if an object is an instance."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the
    specified class. Otherwise false

    Args:
        obj: The object to be checked.
        a_class: The checks to be checked.
    """
    return type(obj) is a_class
