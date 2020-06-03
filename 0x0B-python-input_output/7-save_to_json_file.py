#!/usr/bin/python3
"""Save to json file module
    """
import json


def save_to_json_file(my_obj, filename):
    """Save object with json representation on a file

    Args:
        my_obj (object): object to save on file
        filename (str): File name
    """

    with open(filename, mode='w', encoding='utf8') as a_file:

        my_str = json.dumps(my_obj)
        a_file.write(my_str)
