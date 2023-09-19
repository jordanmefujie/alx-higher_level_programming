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

    def test_initialization_success(self):
        """Initializing class"""

        s1 = Square(5)

        s2 = Square(10)

        self.assertEqual(s1.id, 13)

        self.assertEqual(s2.id, 14)


    def test_initialization_without_arguments(self):
        """Initializing class without arguments"""


        self.assertRaises(TypeError, Square)


if __name__ == '__main__':

    unittest.main()
