#!/usr/bin/python3
def pow_digits(num):
    return num * num


def square_matrix_simple(matrix=[]):
    pow_list = []
    for i in matrix:
        pow_list.append(list(map(pow_digits, i)))
    return pow_list
