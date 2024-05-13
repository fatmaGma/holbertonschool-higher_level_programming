#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in range(len(matrix)):
        for c in range(len(matrix[l])):
            print ("{:d}".format(matrix[l][c]), end ="")
            if c != (len(matrix[l]) - 1):
                print(" ", end="")
        print("")
