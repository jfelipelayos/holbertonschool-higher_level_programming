#!/usr/bin/python3
"""[summary]
    """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8


class TestPep8(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [descriptin]
    """

    def test_pep8(self):
        """[summary]
        """
        pepstyle = pep8.StyleGuide(quiet=True)
        result = pepstyle.check_files(
            ['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
