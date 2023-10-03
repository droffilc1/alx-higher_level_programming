#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print("0{:d}".format(i), end=', ')
    else:
        print("{:d}".format(i), end=', ' if i < 99 else '\n')
