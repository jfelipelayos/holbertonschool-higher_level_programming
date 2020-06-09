#!/usr/bin/python3
"""Unittest for class Square
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch

import unittest
import os
from io import StringIO


class TestSquare(unittest.TestCase):
    """Testing Square
    """

    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Test instantiation
        """
        var1 = Square(5)
        var2 = Square(id="hello", size=3)
        with self.assertRaises(ValueError):
            var3 = Square(-5, 3, 4)
            var4 = Square(9.5, 9.3)
            var5 = Square(float('inf'))
            var6 = Square("string")
            var9 = Square(None)
        with self.assertRaises(TypeError):
            var7 = Square(5, "hi")
            var8 = Square(5, None)
            var10 = Square(5, float('inf'))
            var11 = Square(5, 9.5)
            var12 = Square()
        self.assertEqual(var1.id, 1)

    def test_area(self):
        """Testing area()
        """
        var1 = Square(5)
        var2 = Square(999, 0, 0, "helloo")
        var3 = Square(id="hello", size=3, x=1, y=0)
        self.assertEqual(var1.area(), 25)
        self.assertEqual(var2.area(), 998001)
        self.assertEqual(var3.area(), 9)

    def test_display(self):
        """Testing display()
        """
        var1 = Square(4)
        var2 = Square(id="hello", size=3, x=1, y=0)
        with patch('sys.stdout', new=StringIO()) as str_Output:
            var1.display()
            self.assertEqual(str_Output.getvalue(), '####\n####\n####\n####\n')
        with patch('sys.stdout', new=StringIO()) as str_Output:
            var2.display()
            self.assertEqual(str_Output.getvalue(), ' ###\n ###\n ###\n')

    def test_str(self):
        """Testing __str__()
        """
        var1 = Square(5)
        var2 = Square(3, 2)
        var3 = Square(1, 2, 3, 4)
        self.assertEqual(var1.__str__(), '[Square] (1) 0/0 - 5')
        self.assertEqual(var2.__str__(), '[Square] (2) 2/0 - 3')
        self.assertEqual(var3.__str__(), '[Square] (4) 2/3 - 1')

    def test_update(self):
        """Testing update()
        """
        var1 = Square(5)
        var2 = Square(3, 2)
        var3 = Square(1, 2, 3, 4)
        var4 = Square(id="hello", size=3, x=1, y=0)
        var1.update(6, 1, 2, 8)
        self.assertEqual(var1.__str__(), '[Square] (6) 2/8 - 1')
        var2.update(1, 2, 3, id="hello")
        with self.assertRaises(ValueError):
            var3.update("hello", -5)
            var4.update(x=9.5)

    def test_to_dictionary(self):
        """Testing to_dictionary()
        """
        var1 = Square(5)
        var2 = Square(5, 6)
        var3 = Square(1, 2, 3, 5)
        var4 = Square(3, 2, id="holberton")
        value1 = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        value2 = {'id': 2, 'size': 5, 'x': 6, 'y': 0}
        value3 = {'id': 5, 'size': 1, 'x': 2, 'y': 3}
        value4 = {'id': 'holberton', 'size': 3, 'x': 2, 'y': 0}
        self.assertDictEqual(var1.to_dictionary(), value1)
        self.assertDictEqual(var2.to_dictionary(), value2)
        self.assertDictEqual(var3.to_dictionary(), value3)
        self.assertDictEqual(var4.to_dictionary(), value4)


if __name__ == '__main__':
    unittest.main()
