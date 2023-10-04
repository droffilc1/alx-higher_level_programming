#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(abs(b)):
        res *= a
    # handle negative numbers
    if b < 0:
        return 1 / res
    else:
        return res
