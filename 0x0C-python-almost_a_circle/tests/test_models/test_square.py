#!/usr/bin/python3
"""Test Square class"""

import unittest
import os
import pep8
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square



class TestSquare(unittest.TestCase):
    """Test class square"""

    def test_pep8(self):
        """checks for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0)

        def test_S_integer_size(self):
            """integer validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square({})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(10.1)

    def test_S_integer_x(self):
        """integer validation"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(10, -2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(10, 2.1)

    def test_S_integer_y(self):
        """integer validation"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(10, 3, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 3, 2.1)

    def test_initialization_success(self):
        """Initializing class"""
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 16)
        self.assertEqual(s2.id, 17)

    def test_initialization_without_arguments(self):
        """Initializing class without arguments"""
        self.assertRaises(TypeError, Square)


if __name__ == '__main__':

    unittest.main()
