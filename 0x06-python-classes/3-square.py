#!/usr/bin/python3
"""
Create a Square
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

    def area(self):
        """
        find the area of the square
        """
        return self.__size * self.__size
