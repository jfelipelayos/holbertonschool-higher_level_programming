#!/usr/bin/python3
def no_c(my_string):
    if my_string:

        my_list = list(my_string)

        for i in my_list:
            if i in "Cc":
                my_list.remove(i)
        my_string = "".join(my_list)

        return my_string
