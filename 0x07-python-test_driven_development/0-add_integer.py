#!/usr/bin/python3
"""
add two integers
"""


def add_integer(a, b=98):
    """Add two integers

    Arguments:
        a {int} -- first int to add

    Keyword Arguments:
        b {int} -- second int to add (default: {98})

    Raises:
        TypeError: if a aren't int or float print error
        TypeError: if b aren't int or floar print error
        OverflowError: overflow case
        OverflowError: overflow case

    Returns:
        int -- add of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('NaN') or type(b) is float('NaN'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    return a + b
