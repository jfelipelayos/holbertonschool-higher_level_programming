#!/usr/bin/python3
"""Models module
    """

from models.base import Base

class Rectangle(Base):
    """Define rectangle attributes

    Args:
        Base (class): Super class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super(Rectangle, self).__init__(id)
    
    #Width getter and setter
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    #height getter and setter
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    #x getter and setter
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    #y getter and setter   
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
