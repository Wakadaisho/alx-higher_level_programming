#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_bad_arg_type(self):
        with self.assertRaises(TypeError):
           max_integer(123)
        
    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            max_integer([123, 456], [1, 2], [5, 6])

    def test_ints(self):
        self.assertEqual(max_integer(list(range(-100,100))), 99)

    def test_floats(self):
        self.assertEqual(max_integer([1,2.0,0]), 2.0)

    def test_negatives(self):
        self.assertEqual(max_integer([-1,-2,-10]), -1)

    def test_bad_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 0], 'a')
        with self.assertRaises(TypeError):
            max_integer([1, [], 0], 1)
        with self.assertRaises(TypeError):
            max_integer([1, {}, 0], 1)
        with self.assertRaises(TypeError):
            max_integer([1, (), 0], 1)
