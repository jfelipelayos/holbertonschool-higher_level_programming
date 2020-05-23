#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_beggining(self):
        self.assertEqual(max_integer([7, 5, 3, 1]), 7)

    def test_final(self):
        self.assertEqual(max_integer([4, 5, 6, 7]), 7)

    def test_middle(self):
        self.assertEqual(max_integer([4, 20, 5]), 20)

    def test_negative_number(self):
        self.assertEqual(max_integer([-3, -4, -5]), -3)

    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-1, 2, 1, -2]), 2)

    def test_one_list_size(self):
        self.assertEqual(max_integer([4]), 4)

    def test_other_type(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
