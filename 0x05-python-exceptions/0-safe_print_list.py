#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        el_print = 0
        for i in my_list[:x]:
            print(i, end="")
            el_print += 1
    except IndexError:
        print("Invalid input")
    print()
    return el_print
