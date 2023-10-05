#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} arguments".format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments".format(len(sys.argv) - 1))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
