#!/usr/bin/python3
"""Class to jason module
    """


def class_to_json(obj):
    """Class to JSON

    Args:
        obj (object): object to convert

    Returns:
        object: dict
    """

    return obj.__dict__
