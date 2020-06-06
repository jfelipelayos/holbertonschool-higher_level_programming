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
        return ("[Square] ({:d}) {:d}/{:d} - {:d}").format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return super().width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    