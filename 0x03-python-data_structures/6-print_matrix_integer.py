#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formarted_row = ["{:d}".format(val) for val in row]
        print(" ".join(formarted_row))
