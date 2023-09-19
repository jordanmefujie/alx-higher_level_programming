#!/usr/bin/python3
"""
Test Base class
"""
import pep8
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test for class base"""

    def test_initialization(self):
        """initialization of class base"""

        base1 = Base()

        base2 = Base()

        self.assertEqual(base1.id, 1)

        self.assertEqual(base2.id, 2)

    def test_saving_id(self):
        """Test save id for cass Base"""

        base = Base(100)

        self.assertEqual(base.id, 100)


    def test_to_json_string_valid(self):
        """Test to JSON string"""

        pass


if __name__ == '__main__':

    unittest.main()
