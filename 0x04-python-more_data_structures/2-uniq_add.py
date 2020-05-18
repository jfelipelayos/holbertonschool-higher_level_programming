#!/usr/bin/python3
def uniq_add(my_list=[]):

    acum = 0
    sets = set(my_list)

    for i in sets:
        acum += i
    return (acum)
