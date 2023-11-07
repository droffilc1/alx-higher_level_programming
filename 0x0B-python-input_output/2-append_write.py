#!/usr/bin/python3
"""A module for a function that appends in a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file.

    Args:
        filename: The name of the file.
        text: The text to be written to a file.

    Return:
        The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
