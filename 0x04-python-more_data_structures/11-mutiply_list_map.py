#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):

    new_list = list(map(lambda i: i * number, my_list))

    return new_list
