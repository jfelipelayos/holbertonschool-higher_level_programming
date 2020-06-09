#!/usr/bin/python3
"""Test module
    """

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8
import os


class TestBase(unittest.TestCase):
    """Unit test cases Base

    Args:
        unittest ([type]): [description]
    """
    def test_pep8_conformance_base(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_cero(self):
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_negative(self):
        obj = Base(-1)
        self.assertEqual(obj.id, -1)

        obj = Base(-29837)
        self.assertEqual(obj.id, -29837)

    def test_int(self):
        obj = Base(3)
        self.assertEqual(obj.id, 3)

        obj = Base(1298469)
        self.assertEqual(obj.id, 1298469)

    def test_list(self):
        obj = Base([])
        self.assertEqual(obj.id, [])

        obj = Base([3, 4])
        self.assertEqual(obj.id, [3, 4])

    def test_float(self):
        obj = Base(5.6)
        self.assertEqual(obj.id, 5.6)

        obj = Base(-1.4)
        self.assertEqual(obj.id, -1.4)

    def test_string(self):
        obj = Base('1')
        self.assertEqual(obj.id, '1')

    def test_bool(self):
        obj = Base(True)
        self.assertEqual(obj.id, True)

        obj = Base(False)
        self.assertEqual(obj.id, False)

    def test_tuple(self):
        obj = Base(())
        self.assertEqual(obj.id, ())

        obj = Base((1, 2, 3))
        self.assertEqual(obj.id, (1, 2, 3))

    def test_dict(self):
        obj = Base({"name": "juan", "nick": "name"})
        self.assertEqual(obj.id, {"name": "juan", "nick": "name"})

    # ===============================================================================

    def tearDown(self):
        """tears down obj count
        """
        Base.__Base__nb_objects = 0
        self.assertEqual(Base.__Base__nb_objects, 0)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_instance(self):
        """test instance
        """
        var1 = Base()
        var2 = Base(9)
        var3 = Base(11.5)
        var4 = Base(None)
        var5 = Base("string")
        var6 = Base({})
        var7 = Base(())
        var8 = Base([])

        self.assertEqual(var1.id, 3)
        self.assertEqual(var2.id, 9)
        self.assertEqual(var3.id, 11.5)
        self.assertEqual(var4.id, 4)
        self.assertEqual(var5.id, 'string')
        self.assertEqual(var6.id, {})
        self.assertEqual(var7.id, ())
        self.assertEqual(var8.id, [])

    def test_docstring_base(self):
        """test Docstrings
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_to_json_string(self):
        """test methods to_json_string
        """
        tjs1 = None
        tjs2 = [{"hello": 7}]
        tjs3 = [[1, 4, 8]]
        tjs4 = []

        self.assertCountEqual(Base.to_json_string(tjs1), "[]")
        self.assertCountEqual(Base.to_json_string(tjs2), '[{"hello": 7}]')
        self.assertCountEqual(Base.to_json_string(tjs3), '[[1, 4, 8]]')
        self.assertCountEqual(Base.to_json_string(tjs4), '[]')

    def test_save_to_file(self):
        """test save to file
        """
        pass

    def test_from_json_string(self):
        """test from json string
        """
        tfjs1_expe = [{"Marlon": 47, "García": "Morales"}]
        tfjs1_test = Base.to_json_string(tfjs1_expe)
        self.assertEqual(Base.from_json_string(tfjs1_test), tfjs1_expe)

        tfjs2_expe = [{"Marlon": 47}]
        tfjs2_test = Base.to_json_string(tfjs2_expe)
        self.assertEqual(Base.from_json_string(tfjs2_test), tfjs2_expe)

        tfjs3_expe = []
        tfjs3_test = Base.to_json_string(tfjs3_expe)
        self.assertEqual(Base.from_json_string(tfjs3_test), tfjs3_expe)

        tfjs4_expe = [[1, 4, 8]]
        tfjs4_test = Base.to_json_string(tfjs4_expe)
        self.assertEqual(Base.from_json_string(tfjs4_test), tfjs4_expe)

    def test_create(self):
        """test create
        """
        tc1_expe = {"id": 1, "width": 1, "height": 2, "x": 2, "y": 2}
        tc1_test = Rectangle.create(**tc1_expe)
        self.assertEqual(tc1_test.__str__(), "[Rectangle] (1) 2/2 - 1/2")

        tc2_expe = {"id": 2, "size": 3, "x": 4, "y": 5}
        tc2_test = Square.create(**tc2_expe)
        self.assertEqual(tc2_test.__str__(), "[Square] (2) 4/5 - 3")
        
    def test_load_from_file(self):
        """test create
        """
        tlff1 = Rectangle(10, 7, 2, 8)
        tlff2 = Rectangle(2, 4)

        rect_save = Rectangle.save_to_file([tlff1, tlff2])
        rect_list = Rectangle.load_from_file()

        self.assertIsInstance(rect_list[0], Rectangle)
        self.assertIsInstance(rect_list[1], Rectangle)
        self.assertEqual(rect_list[0].__str__(), "[Rectangle] (5) 2/8 - 10/7")
        self.assertEqual(rect_list[1].__str__(), "[Rectangle] (6) 0/0 - 2/4")

        tlff3 = Square(10, 7, 2)
        tlff4 = Square(8)

        squa_save = Square.save_to_file([tlff3, tlff4])
        squa_list = Square.load_from_file()

        self.assertIsInstance(squa_list[0], Square)
        self.assertIsInstance(squa_list[1], Square)
        self.assertEqual(squa_list[0].__str__(), "[Square] (9) 7/2 - 10")
        self.assertEqual(squa_list[1].__str__(), "[Square] (10) 0/0 - 8")

    def test_style_base(self):
        """test pep8
        """
        style = pep8.StyleGuide()
        m = style.check_files(["models/base.py"])
        self.assertEqual(m.total_errors, 0, "fix pep8")
 
if __name__ == '__main__':
    unittest.main()
