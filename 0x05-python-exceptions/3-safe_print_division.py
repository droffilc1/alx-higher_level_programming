#!/usr/bin/python3
from ctypes import wstring_at


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
