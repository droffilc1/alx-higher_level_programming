#!/usr/bin/python3
"""A module for a function that returns a list."""


def lookup(obj):
    """Returns list of available attributes and methods of an object."""
    return dir(obj)
