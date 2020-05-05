#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if my_list:
        if idx < 0 or idx > len(my_list):
            return my_list

        to_delete = my_list[idx]
        my_list.remove(to_delete)

        return my_list
