#!/usr/bin/python3
"""
Square
"""


class Square:
    """
    Validate a square
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
