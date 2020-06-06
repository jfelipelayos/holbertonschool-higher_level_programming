#!/usr/bin/python3
"""Test module
    """

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Unit test cases Base

    Args:
        unittest ([type]): [description]
    """

    def test_cero(self):
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_void(self):
        obj = Base()
        self.assertEqual(obj.id, 3)

        obj = Base()
        self.assertEqual(obj.id, 4)

        obj = Base()
        self.assertEqual(obj.id, 5)

        obj = Base()
        self.assertEqual(obj.id, 6)

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

    def test_none(self):
        obj = Base(None)
        self.assertEqual(obj.id, 1)

        obj = Base(None)
        self.assertEqual(obj.id, 2)


if __name__ == '__main__':
    unittest.main()
