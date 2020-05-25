#!/usr/bin/python3
"""Define a rectangle
    """


class Rectangle:
    """Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializate variables

        Keyword Arguments:
            width {int} -- Width of the rectangle (default: {0})
            height {int} -- Height of the rectangle (default: {0})
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get rectangle width

        Returns:
            int -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter

        Arguments:
            value {int} -- value of the width

        Raises:
            TypeError: if width isn't an integer print error
            ValueError: if width its less than 0 print error
        """
        if type(value) not in [int]:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get rectangle height

        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter

        Arguments:
            value {int} -- value of the height<

        Raises:
            TypeError: if height isn't an integer print error
            ValueError: if height its less than 0 print error
        """
        if type(value) not in [int]:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('heigt must be >= 0')

        self.__height = value

    def area(self):
        """Find area of the rectangle

        Returns:
            int -- area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Find perimeter of the rectangle

        Returns:
            int -- perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return self.height + self.width + self.height + self.width

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
        for i in range(self.__height):
            rect += (self.print_symbol * self.__width) + '\n'
        return rect

    def __repr__(self):
        """Print rectangle coords

        Returns:
            str -- Rectangle coords
        """
        return 'Rectangle({},{})'.format(self.width, self.height)

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
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        return rect_2
