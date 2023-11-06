#!/usr/bin/python3
"""A module for a function that checks if an object is an instance."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Otherwise False.

    Args:
        obj: The object to be checked.
        a_class: The checks to be checked.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class. Otherwise False.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
