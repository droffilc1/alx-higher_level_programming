"""A module for testing Base class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    """Test Base class."""

    def test_init_with_id(self):
        """Test __init__ method with id."""
        b1 = Base(id=12)
        self.assertEqual(b1.id, 12)

    def test_init_without_id(self):
        """Test __init__ method without id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b3.id, b4.id -1)

    def test_to_json_string(self):
        """ testing test_to_json_string for only one dict
        """
        list_of_dicts = list()
        group_of_dicts = {"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}
        list_of_dicts.append(group_of_dicts)
        str_json = '[{"width": 10, "height": 5, "x": 1, "y": 0, "id": 1}]'
        logic1 = Base.to_json_string(list_of_dicts) == str_json
        self.assertEqual(logic1, True)

    def test_to_json_string_more_than_one_dict(self):
        """ testing test_to_json_string for more than dict
        """
        list_of_dicts = list()
        group_of_dicts = {"width": 10, "height": 7, "x": 2, "y": 6, "id": 1}
        list_of_dicts.append(group_of_dicts)
        group_of2 = {"width": 13, "height": 5, "x": 1, "y": 3, "id": 9}
        list_of_dicts.append(group_of2)
        str_json = '[{"width": 10, "height": 7, "x": 2, "y": 6, "id": 1}, ' +\
                   '{"width": 13, "height": 5, "x": 1, "y": 3, "id": 9}]'
        logic = Base.to_json_string(list_of_dicts) == str_json
        self.assertEqual(logic, True)

    def test_for_empty_list(self):
        """Testing with normal inputs [Empty list]
        """
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_for_empty_dict(self):
        """Edge cases - empty dictionary
        """
        self.assertEqual(Base.to_json_string([{}]), '[{}]')

    def test_for_none(self):
        """Edge cases - None
        """
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_for_square_2_dicts(self):
        """Testing this function with class square
        """
        s1 = Square(4, 7, 6, 5).to_dictionary()
        s2 = Square(5, 5, 5, 5).to_dictionary()
        json_data = Base.to_json_string([s1, s2])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 76)

    def test_for_square_1_dict(self):
        """Testing this function with class square
        """
        s1 = Square(4, 7, 6, 5).to_dictionary()
        json_data = Base.to_json_string([s1])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 38)

    def test_for_rectangle_1_dict(self):
        """Testing for rectangle with 1 dict"""
        rectangle = Rectangle(4, 5, 1, 1).to_dictionary()
        json_data = Base.to_json_string([rectangle])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 52)

    def test_for_rectangle_2_dicts(self):
        """Testing this function with class square
        """
        r1 = Rectangle(4, 7, 6, 5).to_dictionary()
        r2 = Rectangle(5, 5, 5, 5).to_dictionary()
        json_data = Base.to_json_string([r1, r2])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 104)

if __name__ == "__main__":
    unittest.main()
