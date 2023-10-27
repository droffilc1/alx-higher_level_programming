"""Holds a function that prints a string."""

def say_my_name(first_name, last_name=""):
    """Prints two string arguments to the stdout.

    Args:
        first_name: The first argument.
        last_name: The second argument.

    Returns:
        Prints a string to the stdout.

    Raises:
        TypeError: when one or both of the arguments is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
