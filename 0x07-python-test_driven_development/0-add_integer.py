#!/usr/bin/python3
"""
add integer func
"""


def add_integer(a, b=98):
    """Add two integers

    Arguments:
        a {int} -- first number to add

    Keyword Arguments:
        b {int} -- second number to add (default: {98})

    Raises:
        TypeError: if a aren't int or float print error
        TypeError: if b aren't int or floar print error

    Returns:
        int -- add of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
