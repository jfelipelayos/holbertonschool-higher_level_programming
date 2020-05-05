#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    size = len(my_list)

    new_list = my_list.reverse()

    for i in range(0, size):
        print("{}".format(my_list[i]))
