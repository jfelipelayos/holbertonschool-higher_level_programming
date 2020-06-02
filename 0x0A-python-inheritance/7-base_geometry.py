#!/usr/bin/python3
"""[summary]
    """


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """area

        Raises:
            Exception: is not implemented yet
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Integer validator

        Arguments:
            name {str} -- name
            value {int} -- value to validate

        Raises:
            TypeError: if value is not an int raise TypeError
            ValueError: if values is < 0 raise a ValueError
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
