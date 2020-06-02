#!/usr/bin/python3
"""[summary]
    """


class MyList(list):
    """Sort on ascending order

    Arguments:
        list {list} -- list to sort
    """

    def print_sorted(self):
        print(sorted(self))
