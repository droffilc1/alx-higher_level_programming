#!/usr/bin/python3
"""A module with a function that reads a text file."""


def read_file(filename=""):
    """Reads a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
