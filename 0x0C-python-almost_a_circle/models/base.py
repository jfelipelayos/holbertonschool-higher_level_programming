# !/usr/bin/python3
"""Models module
    """
import json


class Base:
    """manage id attribute in all your future classes 
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """

        if list_dictionaries:
            json_representation = json.dumps(list_dictionaries)
        else:
            json_representation = "[]"

        return json_representation

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        with open('{}.json'.format(cls.__name__), mode='w') as f:

            if list_objs:
                json_base_representation = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(json_base_representation))
            else:
                f.write(cls.to_json_string([]))
                
