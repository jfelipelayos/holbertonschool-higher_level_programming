# !/usr/bin/python3
"""Models module
    """
import json


class Base:
    """manage id attribute in all your future classes 
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id = None):

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
        if list_objs:
            new_json_representation = cls.to_json_string(list_objs)
            
            
        else:
            new_json_representation = []
               
        with open("{}.json".format(cls.__name__), encoding='utf8', mode='w') as file:
            file.write(new_json_representation)
        