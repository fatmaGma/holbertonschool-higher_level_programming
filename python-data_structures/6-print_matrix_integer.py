#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for c in l:
            print ("{:d}".format(c), end =" ")
        print()
