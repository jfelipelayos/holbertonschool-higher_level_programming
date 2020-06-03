#!/usr/bin/python3
"""to json string module
    """
import json

def to_json_string(my_obj):
    """Json representation of an object

    Args:
        my_obj (object): object to convert

    Returns:
        json: json representation of the object
    """
    return json.dumps(my_obj)
