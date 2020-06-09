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
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Find area of a rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Display graphic rectangle on stdout
        """
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """str default output

        Returns:
            str: default __str__ output
        """
        return ('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}')\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """[summary]
        """
        if args:
            original_elements = [self.id, self.__width,
                                 self.__height, self.__x, self.__y]

            updated_elements = list(
                args[:len(args)]) + original_elements[len(args):]

            (self.id, self.__width, self.__height,
             self.__x, self.__y) = updated_elements

        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                if i == "width":
                    self.__width = kwargs[i]
                if i == "height":
                    self.__height = kwargs[i]
                if i == "x":
                    self.__x = kwargs[i]
                if i == "y":
                    self.__y = kwargs[i]

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        rectangle_dict = {"id": self.id,
                          "width": self.__width,
                          "height": self.__height,
                          "x": self.__x,
                          "y": self.__y}

        # rectangle_dict = self.__dict__
        return rectangle_dict
