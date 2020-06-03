#!/usr/bin/python3
"""from json string module
    """
import json


def from_json_string(my_str):
    """From json to string

    Args:
        my_str (object): JSON to convert

    Returns:
        dict: object
    """
    return json.loads(my_str)
