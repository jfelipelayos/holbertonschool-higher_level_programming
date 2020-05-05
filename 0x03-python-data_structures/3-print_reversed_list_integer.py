#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    size = len(my_list) - 1

    new_list = my_list.copy()

    for i in range(size, -1, -1):
        print("{}".format(new_list[i]))
