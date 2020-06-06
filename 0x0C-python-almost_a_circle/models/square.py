#!/usr/bin/python3
"""[summary]
    """
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (class): Inheritance
    """

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str default output

        Returns:
            str: default __str__ output
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}")\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        if args:
            original_square_elements = [self.id, self.size, self.x, self.y]

            updated_square_elements = list(
                args[:len(args)]) + original_square_elements[len(args):]

            (self.id, self.size, self.x, self.y) = updated_square_elements

        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                if i == "size":
                    self.size = kwargs[i]
                if i == "x":
                    self.x = kwargs[i]
                if i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        square_dict = {"id": self.id,
                       "size": self.width,
                       "x": self.x,
                       "y": self.y}

        # rectangle_dict = self.__dict__
        return square_dict
