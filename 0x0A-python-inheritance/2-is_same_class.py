#!/usr/bin/python3
"""[summary]
    """


def is_same_class(obj, a_class):
    """Compare if an object is an instance of a class

    Arguments:
        obj {object} -- object to compare
        a_class {class} -- class to compare
    """
    if type(obj) is a_class:
        status = True
    else:
        status = False
    return status
