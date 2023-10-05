#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(count))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
