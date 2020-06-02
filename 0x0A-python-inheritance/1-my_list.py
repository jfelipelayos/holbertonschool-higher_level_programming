#!/usr/bin/python3
"""[summary]
    """


class MyList(list):
    """Sort on ascending order

    Arguments:
        list {list} -- list to sort
    """

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
