#!/usr/bin/python3
"""A module for MyList class"""


class MyList(list):
    """Defines MyList class."""
    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))
