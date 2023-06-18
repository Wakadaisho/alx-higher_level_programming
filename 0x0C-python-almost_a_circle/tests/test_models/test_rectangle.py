#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
import sys
import io

from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def test_init_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_few_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_init_excess_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_min_args(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertNotEqual(rect.id, None)

    def test_max_args(self):
        rect = Rectangle(7, 10, 10, 20, 3)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 20)
        self.assertEqual(rect.id, 3)

    def test_width_type_validation(self):
        with self.assertRaises(TypeError) as width_ex:
            Rectangle("23", 10)
        self.assertEqual(str(width_ex.exception), "width must be an integer")

    def test_width_value_validation(self):
        with self.assertRaises(ValueError) as width_ex:
            Rectangle(0, 10)
        self.assertEqual(str(width_ex.exception), "width must be > 0")

    def test_height_type_validation(self):
        with self.assertRaises(TypeError) as height_ex:
            Rectangle(23, True)
        self.assertEqual(str(height_ex.exception), "height must be an integer")

    def test_height_value_validation(self):
        with self.assertRaises(ValueError) as height_ex:
            Rectangle(23, -3)
        self.assertEqual(str(height_ex.exception), "height must be > 0")

    def test_x_type_validation(self):
        with self.assertRaises(TypeError) as x_ex:
            Rectangle(10, 20, {1}, 5)
        self.assertEqual(str(x_ex.exception), "x must be an integer")

    def test_x_value_validation(self):
        with self.assertRaises(ValueError) as x_ex:
            Rectangle(10, 20, -5, 5)
        self.assertEqual(str(x_ex.exception), "x must be >= 0")

    def test_y_type_validation(self):
        with self.assertRaises(TypeError) as y_ex:
            Rectangle(10, 20, 1, (5,))
        self.assertEqual(str(y_ex.exception), "y must be an integer")

    def test_y_value_validation(self):
        with self.assertRaises(ValueError) as y_ex:
            Rectangle(10, 20, 5, -10)
        self.assertEqual(str(y_ex.exception), "y must be >= 0")

    def test_area(self):
        self.assertEqual(Rectangle(7, 8).area(), 56)

    def test_str(self):
        rect = Rectangle(7, 8, 9, 10, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 9/10 - 7/8")

    def test_update_args(self):
        rect = Rectangle(7, 8, 0, 0, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 7/8")

        rect.update(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_kwargs(self):
        rect = Rectangle(7, 8, 9, 10, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 9/10 - 7/8")

        rect.update(y=1, height=2, x=3, id=4, width=5)
        self.assertEqual(str(rect), "[Rectangle] (4) 3/1 - 5/2")

    def test_to_dictionary(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        dictionary = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertTrue(
                all((rect_dict.get(k) == v for k, v in dictionary.items())))

    def test_display(self):
        rect = Rectangle(3, 4, 1, 1)
        dictionary = io.StringIO()
        sys.stdout = dictionary
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(dictionary.getvalue(), "\n ###\n ###\n ###\n ###\n")
