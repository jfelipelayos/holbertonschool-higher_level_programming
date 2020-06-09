 
#!/usr/bin/python3
"""Test Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestPep8(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """[summary]
        """
        pepstyle = pep8.StyleGuide(quiet=True)
        result = pepstyle.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
