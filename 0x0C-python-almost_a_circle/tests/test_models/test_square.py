#!/usr/bin/python3
"""Unittest for Square
"""
import unittest
import sys
import io

from models.square import Square


class TestSquareClass(unittest.TestCase):
    def test_init_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_init_excess_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)

    def test_min_args(self):
        sq = Square(1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertNotEqual(sq.id, None)

    def test_max_args(self):
        sq = Square(7, 10, 20, 3)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.x, 10)
        self.assertEqual(sq.y, 20)
        self.assertEqual(sq.id, 3)

    def test_size_type_validation(self):
        with self.assertRaises(TypeError) as size_ex:
            Square({45})
        self.assertEqual(str(size_ex.exception), "width must be an integer")

    def test_size_value_validation(self):
        with self.assertRaises(ValueError) as size_ex:
            Square(0)
        self.assertEqual(str(size_ex.exception), "width must be > 0")

    def test_x_type_validation(self):
        with self.assertRaises(TypeError) as x_ex:
            Square(10, {1}, 5)
        self.assertEqual(str(x_ex.exception), "x must be an integer")

    def test_x_value_validation(self):
        with self.assertRaises(ValueError) as x_ex:
            Square(10, -5, 5)
        self.assertEqual(str(x_ex.exception), "x must be >= 0")

    def test_y_type_validation(self):
        with self.assertRaises(TypeError) as y_ex:
            Square(10, 1, (5,))
        self.assertEqual(str(y_ex.exception), "y must be an integer")

    def test_y_value_validation(self):
        with self.assertRaises(ValueError) as y_ex:
            Square(10, 5, -10)
        self.assertEqual(str(y_ex.exception), "y must be >= 0")

    def test_area(self):
        self.assertEqual(Square(7).area(), 49)

    def test_str(self):
        sq = Square(7, 9, 10, 1)
        self.assertEqual(str(sq), "[Square] (1) 9/10 - 7")

    def test_update_args(self):
        sq = Square(7, 0, 0, 1)
        self.assertEqual(str(sq), "[Square] (1) 0/0 - 7")

        sq.update(1, 3, 4, 5)
        self.assertEqual(str(sq), "[Square] (5) 3/4 - 1")

    def test_update_kwargs(self):
        sq = Square(7, 9, 10, 1)
        self.assertEqual(str(sq), "[Square] (1) 9/10 - 7")

        sq.update(y=1, x=3, id=4, size=5)
        self.assertEqual(str(sq), "[Square] (4) 3/1 - 5")

    def test_to_dictionary(self):
        sq_dict = Square(1, 3, 4, 5).to_dictionary()
        dictionary = {'id': 5, 'size': 1, 'x': 3, 'y': 4}
        self.assertTrue(
                all((sq_dict.get(k) == v for k, v in dictionary.items())))

    def test_display(self):
        sq = Square(2, 2, 2)
        dictionary = io.StringIO()
        sys.stdout = dictionary
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(dictionary.getvalue(), "\n\n  ##\n  ##\n")
