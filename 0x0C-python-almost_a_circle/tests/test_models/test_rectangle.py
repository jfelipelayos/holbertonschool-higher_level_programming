#!/bin/usr/python3
"""test rectangle
    """

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8
import io
import sys
from io import StringIO

class TestRectangle(unittest.TestCase):
    """ test
    """
    def tearDown(self):
        """tears down obj count
        """
        Base.__Base__nb_objects = 0
        self.assertEqual(Base.__Base__nb_objects, 0)

    @classmethod 
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.var1 = Rectangle(10, 2)
        cls.var2 = Rectangle(4, 6, 0, 0, 99)

    def test_docstring(self):
        """test Docstrings
        """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
    
    def test_instance_Rect(self):
        """test instance for rectangle
        """
        self.assertEqual(self.var1.id, 1) 
        self.assertEqual(self.var2.id, 99) 
        self.var2.id = "Marlon" 
        self.assertEqual(self.var2.id, "Marlon")

    def test_area(self):
        """test for module area
        """
        self.assertEqual(self.var1.area(), 20)
        self.assertEqual(self.var2.area(), 24)

    def test_display(self): 
        """test module Display
        """
        out1 = Rectangle(3, 5)
        var_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        out1.display()
        sys.stdout = var_stdout
        out1_expe = "###\n" * 5
        self.assertEqual(mystdout.getvalue(), out1_expe)

        out2 = Rectangle(10, 3)
        var_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        out2.display()
        sys.stdout = var_stdout
        out2_expe = "##########\n" * 3
        self.assertEqual(mystdout.getvalue(), out2_expe)

    def test_attr_errors(self):
        """test Errors
        """
        Base._Base__nb_objects = 0 
        with self.assertRaises(TypeError, msg="height must be an integer"): 
            var11 = Rectangle(10, "2") 
        with self.assertRaises(ValueError, msg="height must be > 0"): 
            varr11 = Rectangle(-2, 1) 
        with self.assertRaises(TypeError, msg="width must be an integer"): 
            varr11 = Rectangle({1: 2}, 2) 
        with self.assertRaises(ValueError, msg="width must be > 0"): 
            varr21 = Rectangle(10, 2) 
            varr21.width = -10 
        with self.assertRaises(TypeError, msg="x must be an integer"): 
            varr31 = Rectangle(10, 2) 
            varr31.x = {} 
        with self.assertRaises(ValueError, msg="y must be >=0"): 
            varr41 = Rectangle(10, 2, 3, -1) 

    def test_style_base(self):
        """
        Tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == '__main__': 
    unittest.main()

