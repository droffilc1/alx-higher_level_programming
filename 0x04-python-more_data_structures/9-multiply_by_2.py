#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = 2
    new_dictionary = a_dictionary.copy()
    for key in new_dictionary:
        new_dictionary[key] *= k

    return new_dictionary
