#!/usr/bin/python3
"""Defines Rectangle module"""


import io

import sys

import unittest

from models.base import Base

from models.rectangle import Rectangle



class TestRectangle_instantiation(unittest.TestCase):
    """Test class Rectangle"""

    def _init_(self, width, height, x=0, y=0, id=None):
        """Init function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super()._init_(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y gettet"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the earea of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        space = " "
        for space_y in range(self.__y):
            print()

        for height in range(self.__height):
            print(space * self.__x, end="")
            print("#" * self.__width)

    def _str_(self):
        """String information of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """A public method that assigns an argument to each attribute"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation."""
        return {"id": self.id,
                "width": self._Rectangle__width,
                "height": self._Rectangle__height,
                "x": self._Rectangle__x,
                "y": self._Rectangle__y}

    def test_rectangle_is_base(self):
        """Test rectangler base"""

        self.assertIsInstance(Rectangle(10, 2), Base)


    def test_no_args(self):
        """Test No args"""

        with self.assertRaises(TypeError):

            Rectangle()


    def test_one_arg(self):
        """Test one arg"""

        with self.assertRaises(TypeError):

            Rectangle(1)


    def test_two_args(self):
        """Test two arguments"""

        r1 = Rectangle(10, 2)

        r2 = Rectangle(2, 10)

        self.assertEqual(r1.id, r2.id - 1)


    def test_three_args(self):
        """Test three arguments"""

        r1 = Rectangle(2, 2, 4)

        r2 = Rectangle(4, 4, 2)

        self.assertEqual(r1.id, r2.id - 1)


    def test_four_args(self):
        """Test four arguments"""

        r1 = Rectangle(1, 2, 3, 4)

        r2 = Rectangle(4, 3, 2, 1)

        self.assertEqual(r1.id, r2.id - 1)


    def test_five_args(self):
        """Test five arguments"""

        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)


    def test_more_than_five_args(self):
        """Test more arguments"""

        with self.assertRaises(TypeError):

            Rectangle(1, 2, 3, 4, 5, 6)


    def test_width_private(self):
        """Test width of rectangle"""

        with self.assertRaises(AttributeError):

            print(Rectangle(5, 5, 0, 0, 1).__width)


    def test_height_private(self):
        """Test height of rectangle"""

        with self.assertRaises(AttributeError):

            print(Rectangle(5, 5, 0, 0, 1).__height)


    def test_x_private(self):
        """Test of rectangle attributes x"""

        with self.assertRaises(AttributeError):

            print(Rectangle(5, 5, 0, 0, 1).__x)


    def test_y_private(self):
        """Test of rectangle attributes y"""

        with self.assertRaises(AttributeError):

            print(Rectangle(5, 5, 0, 0, 1).__y)


    def test_width_getter(self):
        """Test width getter"""

        r = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(5, r.width)


    def test_width_setter(self):
        """Test width setter"""

        r = Rectangle(5, 7, 7, 5, 1)

        r.width = 10

        self.assertEqual(10, r.width)


    def test_height_getter(self):
        """Test height getter of rectangle"""

        r = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(7, r.height)


    def test_height_setter(self):
        """Test height rectangle setter"""

        r = Rectangle(5, 7, 7, 5, 1)

        r.height = 10

        self.assertEqual(10, r.height)


    def test_x_getter(self):
        """Test x getter of rectangle"""

        r = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(7, r.x)


    def test_x_setter(self):
        """Test rectangle setter x"""

        r = Rectangle(5, 7, 7, 5, 1)

        r.x = 10

        self.assertEqual(10, r.x)


    def test_y_getter(self):
        """Test rectangle getter y"""

        r = Rectangle(5, 7, 7, 5, 1)

        self.assertEqual(5, r.y)


    def test_y_setter(self):
        """Test y setter of rectangle"""

        r = Rectangle(5, 7, 7, 5, 1)

        r.y = 10

        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):

    """Unittests fordth attribute."""


    def test_None_width(self):
        """Test for attribute none"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(None, 2)


    def test_str_width(self):
        """Test for attribute str"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle("invalid", 2)


    def test_float_width(self):
        """Test for attribute float"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(5.5, 1)


    def test_complex_width(self):
        """Test attributes for complex"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(complex(5), 2)


    def test_dict_width(self):
        """Test dictionary"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle({"a": 1, "b": 2}, 2)


    def test_bool_width(self):
        """Test for boolean value"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(True, 2)


    def test_list_width(self):
        """Test list"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle([1, 2, 3], 2)


    def test_set_width(self):
        """Test for set"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle({1, 2, 3}, 2)


    def test_tuple_width(self):
        """Test for tuple"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle((1, 2, 3), 2)


    def test_frozenset_width(self):
        """Test for frozenset"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(frozenset({1, 2, 3, 1}), 2)


    def test_range_width(self):
        """Test range"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(range(5), 2)


    def test_bytes_width(self):
        """Test bytes"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(b'Python', 2)


    def test_bytearray_width(self):
        """Test for bytearray"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(bytearray(b'abcdefg'), 2)


    def test_memoryview_width(self):
        """Test of memory"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(memoryview(b'abcedfg'), 2)


    def test_inf_width(self):
        """Test for infomation"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(float('inf'), 2)


    def test_nan_width(self):
        """Test for nan"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle(float('nan'), 2)


    def test_negative_width(self):
        """Test for negative case"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            Rectangle(-1, 2)


    def test_zero_width(self):
        """Test for zero case"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            Rectangle(0, 2)

class TestRectangle_height(unittest.TestCase):

    """Unittests for testing Rectangle height attribute."""


    def test_None_height(self):
        """Test no case"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, None)


    def test_str_height(self):
        """Test string"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, "invalid")


    def test_float_height(self):
        """Test for float cases"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, 5.5)


    def test_complex_height(self):
        """Test for complex cases"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, complex(5))


    def test_dict_height(self):
        """Test dict"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, {"a": 1, "b": 2})


    def test_list_height(self):
        """test list"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, [1, 2, 3])


    def test_set_height(self):
        """Test set """

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, {1, 2, 3})


    def test_tuple_height(self):
        """Test tuple"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, (1, 2, 3))


    def test_frozenset_height(self):
        """Test frozenset"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, frozenset({1, 2, 3, 1}))


    def test_range_height(self):
        """Test range"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, range(5))


    def test_bytes_height(self):
        """Test byte """

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, b'Python')


    def test_bytearray_height(self):
        """Test bytearray"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, bytearray(b'abcdefg'))


    def test_memoryview_height(self):
        """Test byte memory"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, memoryview(b'abcedfg'))


    def test_inf_height(self):
        """Test info"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, float('inf'))


    def test_nan_height(self):
        """Test for nan"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, float('nan'))


    def test_negative_height(self):
        """Test for negative cases"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            Rectangle(1, -1)


    def test_zero_height(self):
        """Test for zero cases"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            Rectangle(1, 0)



class TestRectangle_x(unittest.TestCase):

    """Unittests for testing Rectangle x attribute."""


    def test_None_x(self):
        """Test none"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, None)


    def test_str_x(self):
        """Test str x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, "invalid", 2)


    def test_float_x(self):
        """Test for float x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, 5.5, 9)


    def test_complex_x(self):
        """Test for complex cases of x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, complex(5))


    def test_dict_x(self):
        """Test dict x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, {"a": 1, "b": 2}, 2)


    def test_bool_x(self):
        """Test boolean value"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, True, 2)


    def test_list_x(self):
        """Test list"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, [1, 2, 3], 2)


    def test_set_x(self):
        """Test set x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, {1, 2, 3}, 2)


    def test_tuple_x(self):
        """Test tuple x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, (1, 2, 3), 2)


    def test_frozenset_x(self):
        """Test fronzenset cases of x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, frozenset({1, 2, 3, 1}))


    def test_range_x(self):
        """Test range of x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, range(5))


    def test_bytes_x(self):
        """Test bytes"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, b'Python')


    def test_bytearray_x(self):
        """Test bytearray"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, bytearray(b'abcdefg'))


    def test_memoryview_x(self):
        """Test memory """

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, memoryview(b'abcedfg'))


    def test_inf_x(self):
        """Test infomation"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, float('inf'), 2)


    def test_nan_x(self):
        """Test nan cases"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, float('nan'), 2)


    def test_negative_x(self):
        """Test negative cases """

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):

            Rectangle(5, 3, -1, 0)



class TestRectangle_y(unittest.TestCase):

    """Unittests for testing initiaon of Rect y attribute."""


    def test_None_y(self):
        """Test none"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, None)


    def test_str_y(self):
        """Test str y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, "invalid")


    def test_float_y(self):
        """Test float of y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, 5.5)


    def test_complex_y(self):
        """Test complex cases"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, complex(5))


    def test_dict_y(self):
        """Test dict"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, {"a": 1, "b": 2})


    def test_list_y(self):
        """Test list"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, [1, 2, 3])


    def test_set_y(self):
        """Test set"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, {1, 2, 3})


    def test_tuple_y(self):
        """Test tuple"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, (1, 2, 3))


    def test_frozenset_y(self):
        """Test fronzenset"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))


    def test_range_y(self):
        """Test range"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, range(5))


    def test_bytes_y(self):
        """Test bytes"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, b'Python')


    def test_bytearray_y(self):
        """Test bytearray"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, bytearray(b'abcdefg'))


    def test_memoryview_y(self):
        """Test memory"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 3, memoryview(b'abcedfg'))


    def test_inf_y(self):
        """Test info"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, float('inf'))


    def test_nan_y(self):
        """Test nan"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            Rectangle(1, 2, 1, float('nan'))


    def test_negative_y(self):
        """Test negative"""

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):

            Rectangle(3, 5, 0, -1)



class TestRectangle_order_of_initialization(unittest.TestCase):

    """Unittests for testie."""


    def test_width_before_height(self):
        """Test width before height"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle("invalid width", "invalid height")


    def test_width_before_x(self):
        """Test width before"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle("invalid width", 2, "invalid x")


    def test_width_before_y(self):
        """Test width before y"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            Rectangle("invalid width", 2, 3, "invalid y")


    def test_height_before_x(self):
        """Test height before x"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, "invalid height", "invalid x")


    def test_height_before_y(self):
        """Test height before y"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            Rectangle(1, "invalid height", 2, "invalid y")


    def test_x_before_y(self):
        """Test x before y"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            Rectangle(1, 2, "invalid x", "invalid y")



class TestRectangle_area(unittest.TestCase):

    """Unittests for testing the area ±± tttyy of the Rectangle class."""


    def test_area_small(self):
        """Test small area of rectangle"""

        r = Rectangle(10, 2, 0, 0, 0)

        self.assertEqual(20, r.area())


    def test_area_large(self):
        """Test large area of rectangle"""

        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)

        self.assertEqual(999999999999998999000000000000001, r.area())


    def test_area_changed_attributes(self):
        """Test area for changed attributes"""

        r = Rectangle(2, 10, 1, 1, 1)

        r.width = 7

        r.height = 14

        self.assertEqual(98, r.area())


    def test_area_one_arg(self):
        """Test area one"""

        r = Rectangle(2, 10, 1, 1, 1)

        with self.assertRaises(TypeError):

            r.area(1)



class TestRectangle_stdout(unittest.TestCase):

    """Unittests for testing __str__ and display  &&&& of Rectangle class."""


    @staticmethod

    def capture_stdout(rect, method):

        """Captures and returns text &&&&&&  printed to stdout.

        """

        capture = io.StringIO()

        sys.stdout = capture

        if method == "print":

            print(rect)

        else:

            rect.display()

        sys.stdout = sys.__stdout__

        return capture


    # Test __str__ method

    def test_str_method_print_width_height(self):
        """Test str method"""

        r = Rectangle(4, 6)

        capture = TestRectangle_stdout.capture_stdout(r, "print")

        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)

        self.assertEqual(correct, capture.getvalue())


    def test_str_method_width_height_x(self):
        """Test str method width of height x"""

        r = Rectangle(5, 5, 1)

        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)

        self.assertEqual(correct, r.__str__())


    def test_str_method_width_height_x_y(self):
        """Test str method width height x and y"""

        r = Rectangle(1, 8, 2, 4)

        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)

        self.assertEqual(correct, str(r))


    def test_str_method_width_height_x_y_id(self):
        """Test str methods"""

        r = Rectangle(13, 21, 2, 4, 7)

        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))


    def test_str_method_changed_attributes(self):
        """Test str method changed attributes"""

        r = Rectangle(7, 7, 0, 0, [4])

        r.width = 15

        r.height = 1

        r.x = 8

        r.y = 10

        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))


    def test_str_method_one_arg(self):
        """Test str method with one arguments"""

        r = Rectangle(1, 2, 3, 4, 5)

        with self.assertRaises(TypeError):

            r.__str__(1)


    # Test display method

    def test_display_width_height(self):
        """Test display width height"""

        r = Rectangle(2, 3, 0, 0, 0)

        capture = TestRectangle_stdout.capture_stdout(r, "display")

        self.assertEqual("##\n##\n##\n", capture.getvalue())


    def test_display_width_height_x(self):
        """Test display width height x"""

        r = Rectangle(3, 2, 1, 0, 1)

        capture = TestRectangle_stdout.capture_stdout(r, "display")

        self.assertEqual(" ###\n ###\n", capture.getvalue())


    def test_display_width_height_y(self):
        """Test display width height y"""

        r = Rectangle(4, 5, 0, 1, 0)

        capture = TestRectangle_stdout.capture_stdout(r, "display")

        display = "\n####\n####\n####\n####\n####\n"

        self.assertEqual(display, capture.getvalue())


    def test_display_width_height_x_y(self):
        """Test display width height x and y"""

        r = Rectangle(2, 4, 3, 2, 0)

        capture = TestRectangle_stdout.capture_stdout(r, "display")

        display = "\n\n   ##\n   ##\n   ##\n   ##\n"

        self.assertEqual(display, capture.getvalue())


    def test_display_one_arg(self):
        """Test display one arguments"""

        r = Rectangle(5, 1, 2, 4, 7)

        with self.assertRaises(TypeError):

            r.display(1)



class TestRectangle_update_args(unittest.TestCase):

    """Unittests for testing updatess."""


    # Test args

    def test_update_args_zero(self):
        """test_update_args zero"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update()

        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


    def test_update_args_one(self):
        """test_update_args one"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89)

        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))


    def test_update_args_two(self):
        """test_update_args two"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))


    def test_update_args_three(self):
        """test_update_args three"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, 3)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))


    def test_update_args_four(self):
        """test_update_args four"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, 3, 4)

        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))


    def test_update_args_five(self):
        """test_update_args five"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, 3, 4, 5)

        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))


    def test_update_args_more_than_five(self):
        """test_update_args more than five"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, 3, 4, 5, 6)

        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))


    def test_update_args_None_id(self):
        """test_update_args None id"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(None)

        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)

        self.assertEqual(correct, str(r))


    def test_update_args_None_id_and_more(self):
        """test_update_args None id and more"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(None, 4, 5, 2)

        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)

        self.assertEqual(correct, str(r))


    def test_update_args_twice(self):
        """test_update_args twice"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, 3, 4, 5, 6)

        r.update(6, 5, 4, 3, 2, 89)

        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))


    def test_update_args_invalid_width_type(self):
        """test_update_args invalid width type"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            r.update(89, "invalid")


    def test_update_args_width_zero(self):
        """test_update_args width zero"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            r.update(89, 0)


    def test_update_args_width_negative(self):
        """test_update_args width negative"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            r.update(89, -5)


    def test_update_args_invalid_height_type(self):
        """test_update_args invalid height type"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            r.update(89, 2, "invalid")


    def test_update_args_height_zero(self):
        """test_update_args height zero"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            r.update(89, 1, 0)


    def test_update_args_height_negative(self):
        """test_update_args height negative"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            r.update(89, 1, -5)


    def test_update_args_invalid_x_type(self):
        """test_update_args invalid x type"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            r.update(89, 2, 3, "invalid")


    def test_update_args_x_negative(self):
        """test_update_args x negative"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):

            r.update(89, 1, 2, -6)


    def test_update_args_invalid_y(self):
        """test_update args invalid y"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            r.update(89, 2, 3, 4, "invalid")


    def test_update_args_y_negative(self):
        """test_update args y negative"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):

            r.update(89, 1, 2, 3, -6)


    def test_update_args_width_before_height(self):
        """test_update_args width before height"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            r.update(89, "invalid", "invalid")


    def test_update_args_width_before_x(self):
        """test_update_args width before x"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            r.update(89, "invalid", 1, "invalid")


    def test_update_args_width_before_y(self):
        """test_update_args width before y"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            r.update(89, "invalid", 1, 2, "invalid")


    def test_update_args_height_before_x(self):
        """test_update_args height before x"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            r.update(89, 1, "invalid", "invalid")


    def test_update_args_height_before_y(self):
        """test_update_args height before y"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            r.update(89, 1, "invalid", 1, "invalid")


    def test_update_args_x_before_y(self):
        """test_update_args x before y"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            r.update(89, 1, 2, "invalid", "invalid")



class TestRectangle_update_kwargs(unittest.TestCase):

    """Unittests for testing update kwargs of the Rectangle class."""

    def test_update_kwargs_one(self):
        """Test kwargs on one"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(id=1)

        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))


    def test_update_kwargs_two(self):
        """Test kwargs on two"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(width=2, id=1)

        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))


    def test_update_kwargs_three(self):
        """Test kwargs on three"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(width=2, height=3, id=89)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))


    def test_update_kwargs_four(self):
        """Test kwargs on four"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(id=89, x=1, height=2, y=3, width=4)

        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))


    def test_update_kwargs_five(self):
        """Test kwargs on five"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(y=5, x=8, id=99, width=1, height=2)

        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))


    def test_update_kwargs_None_id(self):
        """Test none updates"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(id=None)

        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)

        self.assertEqual(correct, str(r))


    def test_update_kwargs_None_id_and_more(self):
        """Test none ids"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(id=None, height=7, y=9)

        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)

        self.assertEqual(correct, str(r))


    def test_update_kwargs_twice(self):
        """Test updates kwargs twice"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(id=89, x=1, height=2)

        r.update(y=3, height=15, width=2)

        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))


    def test_update_kwargs_invalid_width_type(self):
        """Test invalid width"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):

            r.update(width="invalid")


    def test_update_kwargs_width_zero(self):
        """Test cases with zero"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            r.update(width=0)


    def test_update_kwargs_width_negative(self):
        """Test cases with negative"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):

            r.update(width=-5)


    def test_update_kwargs_invalid_height_type(self):
        """Test for invalid type kwargs"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):

            r.update(height="invalid")


    def test_update_kwargs_height_zero(self):
        """Test for zero cases"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            r.update(height=0)


    def test_update_kwargs_height_negative(self):
        """Test updates for negative cases"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):

            r.update(height=-5)


    def test_update_kwargs_inavlid_x_type(self):
        """Test for invalid types of x"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):

            r.update(x="invalid")


    def test_update_kwargs_x_negative(self):
        """Test for negative cases"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):

            r.update(x=-5)


    def test_update_kwargs_invalid_y_type(self):
        """Test for invalid types of y"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):

            r.update(y="invalid")


    def test_update_kwargs_y_negative(self):
        """Updates on negative kwargs"""

        r = Rectangle(10, 10, 10, 10, 10)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):

            r.update(y=-5)


    def test_update_args_and_kwargs(self):
        """Test updates on arguments and kwargs"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(89, 2, height=4, y=6)

        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))


    def test_update_kwargs_wrong_keys(self):
        """Test updates on wrong keys"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(a=5, b=10)

        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


    def test_update_kwargs_some_wrong_keys(self):
        """Test on updates"""

        r = Rectangle(10, 10, 10, 10, 10)

        r.update(height=5, id=89, a=1, b=54, x=19, y=7)

        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))



class TestRectangle_to_dictionary(unittest.TestCase):

    """Unittr testin>iiiiiiii ctionary of the Rectangle class."""


    def test_to_dictionary_output(self):
        """Test Dict output"""

        r = Rectangle(10, 2, 1, 9, 5)

        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}

        self.assertDictEqual(correct, r.to_dictionary())


    def test_to_dictionary_no_object_changes(self):
        """Test dict without object"""

        r1 = Rectangle(10, 2, 1, 9, 5)

        r2 = Rectangle(5, 9, 1, 2, 10)

        r2.update(**r1.to_dictionary())

        self.assertNotEqual(r1, r2)


    def test_to_dictionary_arg(self):
        """Test dict"""

        r = Rectangle(10, 2, 4, 1, 2)

        with self.assertRaises(TypeError):

            r.to_dictionary(1)



if __name__ == "__main__":

    unittest.main()
