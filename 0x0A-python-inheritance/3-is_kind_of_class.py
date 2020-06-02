#!/usr/bin/python3
"""function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
    """


def is_kind_of_class(obj, a_class):
    """Find if an object is an instace of a class

    Arguments:
        obj {object} -- object to compare
        a_class {class} -- class to compare

    Returns:
        bool -- true if its instance, otherwise false.
    """

    status = isinstance(obj, a_class)
    return status
