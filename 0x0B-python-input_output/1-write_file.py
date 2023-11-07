#!/usr/bin/python3
"""A module for a function that writes in a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Args:
        filename: The name of the file.
        text: The text to be written to a file.

    Return:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
