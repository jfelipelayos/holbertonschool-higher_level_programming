#!/usr/bin/python3
"""
Find a square and print it with the size specified
the spaces specified and the position specified
"""


class Square:
    """
    Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Class constructor
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size setter
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Position getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Position Setter
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        find the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square in a graphical way
        """
        if self.size != 0:
            if self.position[1] is not 0:
                print('\n' * self.position[1], end='')
            for ch in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()
