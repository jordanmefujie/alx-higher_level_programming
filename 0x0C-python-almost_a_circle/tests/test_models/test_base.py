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

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_BaseMethods(self):
        """check for methods"""
        self.assertTrue(Base._init.__doc_)
        self.assertTrue(Base.to_json_string._doc_)
        self.assertTrue(Base.save_to_file._doc_)
        self.assertTrue(Base.from_json_string._doc_)
        self.assertTrue(Base.create._doc_)
        self.assertTrue(Base.load_from_file._doc_)


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


        def test_to_json(self):
            """test to_json string task"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dicti = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dict = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """test save_to_file task"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))

    def test_from_json(self):
        """Tests from_json_string task"""
        st_in = '[{"id": 89, "width": 10, "height": 4},\
{"id": 7, "width": 1, "height": 7}]'
        empty_ls = []
        st_out = Rectangle.from_json_string(st_in)
        self.assertEqual(len(st_out), 2)


    def test_to_json_string_valid(self):
        """Test to JSON string"""

        pass


if __name__ == '__main__':

    unittest.main()
