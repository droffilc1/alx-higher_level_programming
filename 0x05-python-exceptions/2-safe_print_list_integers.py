#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    el_print = 0
    for item in my_list[:x]:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                el_print += 1
        except ValueError:
            pass
    print()
    return el_print
