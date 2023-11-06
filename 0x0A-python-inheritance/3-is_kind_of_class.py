#!/usr/bin/python3
"""A module for a function that checks if an object is an instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is exactly an instance of, or if the
    object is an instance of a a class that inherited from  the specified
    class. Otherwise False.

    Args:
        obj: The object to be checked.
        a_class: The checks to be checked.
    """
    return isinstance(obj, a_class)
