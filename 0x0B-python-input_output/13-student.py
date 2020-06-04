#!/usr/bin/python3
"""Student module
    """


class Student:
    """[summary]
    """

    def __init__(self, first_name, last_name, age):
        """init method

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json to dict

        Returns:
            object: object to dict
        """
        n_dict = {}

        if attrs is None:
            return self.__dict__

        for i in attrs:
            if hasattr(self, i):
                n_dict[i] = getattr(self, i)
        return n_dict

    def reload_from_json(self, json):
        """reload

        Args:
            json (json): json
        """
        for i, x in json.items():
            self.__dict__[i] = x
