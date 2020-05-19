#!/usr/bin/python3
"""
Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Class constructor
        Parameter size: size of the square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        find the area of the square
        """
        return self.__size * self.__size
