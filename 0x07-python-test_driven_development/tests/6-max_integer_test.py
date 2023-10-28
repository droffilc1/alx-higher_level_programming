#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This is a max integer test"""
    def test_max_integer(self):
        """Test for max integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer(['1', '2', '3', '4']), '4')

    def test_types(self):
        """Test for different types"""
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, True)
