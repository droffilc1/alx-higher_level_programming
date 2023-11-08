#!/usr/bin/python3
"""A module for a function that inserts text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename: The name of the file.
        search_string: The string to be seached.
        new_string: The string to be added.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
