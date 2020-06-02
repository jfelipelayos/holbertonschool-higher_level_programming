#!/usr/bin/python3
"""function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """List of available attributes and methods

    Arguments:
        obj {object} -- object to find attributes and methods

    Returns:
        list -- available attributes and methods
    """
    return (dir(obj))
