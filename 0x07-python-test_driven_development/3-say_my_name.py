#!/usr/bin/python3
"""
Say my name func
"""


def say_my_name(first_name, last_name=""):
    """Print a hello mesagge with Name and last name

    Arguments:
        first_name {str} -- first name

    Keyword Arguments:
        last_name {str} -- last name (default: {""})

    Raises:
        TypeError: if first name isn't a str print error message
        TypeError: if las name isn't a str print error message
    """

    if type(first_name) not in [str]:
        raise TypeError('first_name must be a string')

    if type(last_name) not in [str]:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
