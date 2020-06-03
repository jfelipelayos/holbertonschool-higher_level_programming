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

    def to_json(self):
        """json to dict

        Returns:
            object: object to dict
        """
        return self.__dict__
