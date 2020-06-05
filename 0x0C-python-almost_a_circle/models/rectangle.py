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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    # Width getter and setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    # height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Integer validator
        Arguments:
            name {str} -- name
            value {int} -- value to validate
        Raises:
            TypeError: if value is not an int raise TypeError
            ValueError: if values is < 0 raise a ValueError
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            if name == "width" or name == "height":
                raise ValueError('{} must be > 0'.format(name))
            else:
                raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """Find area of a rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Display graphic rectangle on stdout
        """

        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """str default output

        Returns:
            str: default __str__ output
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}')\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
