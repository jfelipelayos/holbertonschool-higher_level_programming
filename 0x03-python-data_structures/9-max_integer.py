#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None

    size = len(my_list)

    max_num = my_list[0]

    for i in range(0, size):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return (max_num)
