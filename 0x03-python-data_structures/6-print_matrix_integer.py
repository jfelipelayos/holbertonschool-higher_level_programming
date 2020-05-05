#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for m in matrix:
        for n in range(len(m)):
            if n != len(m) - 1:
                print("{:d}".format(m[n]), end=" ")
            else:
                print("{:d}".format(m[n]), end="")
        print()
