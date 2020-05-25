#!/usr/bin/python3
"""define Rectrangle

    Raises:
        TypeError: rectangle width must be an integer
        ValueError: rectangle width must be > 0
        TypeError: rectangle height must be an integer
        ValueError: rectangle height must be an integer
    """


class Rectangle:
    """Rectangle class
    """

    def __init__(self, width=0, height=0):
        """init rectangle

        Keyword Arguments:
            width {int} -- Rectangle width (default: {0})
            height {int} -- Rectangle height (default: {0})
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get rectangle width

        Returns:
            int -- rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set rectangle width
        Arguments:
            value (int) -- rectangle width
        Raises:
            TypeError: width must be an integer.
            TypeError: width must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get rectangle height

        Returns:
            int -- rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set rectangle height
        Arguments:
            value (int) -- rectangle height.
        Raises:
            TypeError: height must be an integer.
            TypeError: height must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Find area of the rectangle

        Returns:
            int -- area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Find perimeter of the rectangle

        Returns:
            int -- perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height + self.__width + self.__height + self.__width

    def __str__(self):
        """Print rectangle

        Returns:
            str -- rectangle
        """
        rect = ''
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            rect += ("#" * self.__width) + '\n'
        return rect
