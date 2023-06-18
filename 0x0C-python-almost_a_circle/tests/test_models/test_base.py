#!/usr/bin/python3
"""Unittest for Base using Square
"""
import unittest

from models.square import Square
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_id(self):
        b = Base(7)
        self.assertTrue(b.id == 7)

    def test_id_increment(self):
        b = Base()
        self.assertTrue(b.id == 1)
        b_2 = Base()
        self.assertTrue(b_2.id == 2)

    def test_excess_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_empty_none_to_json_string(self):
        json_none = Base.to_json_string(None)
        self.assertEqual(json_none, "[]")
        json_empty = Base.to_json_string([])
        self.assertEqual(json_empty, "[]")

    def test_dict_from_to_json_string(self):
        d = {"id": 1, "size": 2, "x": 3, "y": 4}
        json = Base.to_json_string([d])
        original = Base.from_json_string(json)
        self.assertTrue(
                all((d.get(k) == v for k, v in (original[0].items()))))

    def test_create(self):
        sq = Square(1, 2, 3, 4)
        new_sq = Square.create(**(sq.to_dictionary()))
        self.assertEqual(str(sq), '[Square] (4) 2/3 - 1')
        self.assertEqual(str(new_sq), '[Square] (4) 2/3 - 1')
        self.assertFalse(id(sq) == id(new_sq))

    def test_save_load_file_json(self):
        sq_a = Square(10, 0, 0, -1)
        sq_b = Square(2, 1, 1, -2)
        Square.save_to_file([sq_a, sq_b])
        (sq_a_2, sq_b_2) = Square.load_from_file()
        self.assertEqual(str(sq_a), str(sq_a_2))
        self.assertEqual(str(sq_b), str(sq_b_2))

    def test_save_load_file_csv(self):
        sq_a = Square(10, 0, 0, 1)
        sq_b = Square(2, 1, 1, 2)
        Square.save_to_file_csv([sq_a, sq_b])
        (sq_a_2, sq_b_2) = Square.load_from_file_csv()
        self.assertEqual(str(sq_a), str(sq_a_2))
        self.assertEqual(str(sq_b), str(sq_b_2))
