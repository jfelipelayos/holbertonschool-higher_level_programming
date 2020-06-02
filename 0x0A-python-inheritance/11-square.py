#!/usr/bin/python3
"""[summary]
    """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square

    Arguments:
        Rectangle {class} -- Rectangle
    """

    def __init__(self, size):
        """init method

        Arguments:
            size {int} -- size of the square
        """
        self.integer_validator("size", size)

        self.__size = size

    def __str__(self):
        return('[Square] {}/{}'.format(self.__size, self.__size))

    def area(self):
        """find a Square area

        Returns:
            int -- area of the square
        """
        return (self.__size * self.__size)
