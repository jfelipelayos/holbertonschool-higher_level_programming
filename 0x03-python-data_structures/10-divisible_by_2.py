#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    result = []

    size = len(my_list)

    for i in range(0, size):

        if my_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
