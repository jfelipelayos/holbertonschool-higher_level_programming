#!/usr/bin/python3
"""Models module
    """

import json
import turtle
import random
import time


class Base():
    """[summary]

    Returns:
        [type]: [description]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """

        if list_dictionaries:
            json_representation = json.dumps(list_dictionaries)
        else:
            json_representation = "[]"

        return json_representation

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        with open('{}.json'.format(cls.__name__), mode='w') as f:

            if list_objs:
                base_json_representation = [
                    obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(base_json_representation))
            else:
                f.write(cls.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        if cls.__name__ == "Rectangle":
            lst = cls(1, 1)
        if cls.__name__ == "Square":
            lst = cls(1)
        lst.update(**dictionary)
        return lst

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        try:
            with open("{}.json".format(cls.__name__), mode="r") as f:
                instances_list = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in instances_list]

        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):

        win = turtle.Screen()
        turtle.title("Almost a circle")

        win.bgcolor("black")

        colors_square = ["green yellow", "dark cyan", "medium slate blue"]
        colors_rectangle = ["turquoise", "yellow", "magenta"]

        turtle.setup(1080, 720)
        turtle.shape("square")
        turtle.speed(2)
        turtle.pensize(4)

        for rectangle in list_rectangles:
            turtle.goto(random.randint(-350, 100), random.randint(-350, 100))
            turtle.pendown()
            for i in range(4):
                turtle.color(random.choice(colors_rectangle))
                turtle.forward(rectangle.width if i %
                               2 == 0 else rectangle.height)
                turtle.left(90)
            turtle.penup()
            turtle.color("white")
            turtle.write(rectangle, font=("Arial", 15, "bold"))
            time.sleep(2)

        for square in list_squares:
            turtle.goto(random.randint(-350, 100), random.randint(-350, 100))
            turtle.pendown()
            for i in range(4):
                turtle.color(random.choice(colors_square))
                turtle.forward(square.width)
                turtle.left(90)
            turtle.penup()
            turtle.color("white")
            turtle.write(square, font=("Arial", 15, "bold"))
            time.sleep(2)

        turtle.done()
        turtle.bye()
