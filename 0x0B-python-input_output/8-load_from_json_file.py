#!/usr/bin/python3
"""Load from json file
    """
import json


def load_from_json_file(filename):
    """load from json

    Args:
        filename (str): file name

    Returns:
        object: resulted object
    """
    with open(filename) as a_file:
        my_obj = json.load(a_file)
    return (my_obj)
