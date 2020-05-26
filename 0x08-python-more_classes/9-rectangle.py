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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle

        Keyword Arguments:
            width {int} -- Rectangle width (default: {0})
            height {int} -- Rectangle height (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(self.print_symbol) is not str:
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height - 1):
            rect += (self.print_symbol * self.__width) + '\n'
        rect += (self.print_symbol * self.__width)
        return rect

    def __repr__(self):
        """Print rectangle coords

        Returns:
            str -- Rectangle coords
        """
        return 'Rectangle({},{})'.format(self.__width, self.__height)

    def __del__(self):
        """Delete an attribute
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find the biggest instance or equals

        Arguments:
            rect_1 {Rectangle} -- Rectangle instance to compare
            rect_2 {Rectangle} -- Rectangle instance to compare

        Raises:
            TypeError: If first rectangle itsn't a Rectangle instance
            TypeError: If second rectangle itsn't a Rectangle instance

        Returns:
            Rectangle -- Biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return rect_2

    @classmethod
    def square(cls, size=0):
        """square

        Keyword Arguments:
            size {int} -- size of the square (default: {0})

        Returns:
            Rectangle -- rentangle with the specified size
        """
        return cls(size, size)
