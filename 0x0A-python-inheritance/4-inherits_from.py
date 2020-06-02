#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Find if an object is a subclass

    Arguments:
        obj {object} -- object to compare
        a_class {class} -- class to compare

    Returns:
        bool -- True if the object is subclass, otherwise False.
    """

    status = issubclass(type(obj), a_class)
    return status
