"""This module provides a function that prints 2 new lines
after certain characters.
"""

def text_indentation(text):
    """This function divides prints 2 new lines after each
    of these characters: ., ?, and :.

    Args:
        text: A string.

    Returns:
        prints 2 new lines after certain characters

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
