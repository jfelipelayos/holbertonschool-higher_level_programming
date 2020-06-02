#!/usr/bin/python3
"""[summary]
    """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle

    Arguments:
        BaseGeometry {BaseGeometry} -- Super Class
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
