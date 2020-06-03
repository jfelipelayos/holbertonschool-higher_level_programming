#!/usr/bin/python3
"""[summary]
    """


def add_attribute(obj, name, value):
    """add attribute

    Arguments:
        obj {object} -- object to add
        name {str} -- name
        value {int} -- value

    Raises:
        TypeError: if isn't posible to create raise an error
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
