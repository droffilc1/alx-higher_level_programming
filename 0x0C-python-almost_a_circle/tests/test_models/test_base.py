"""A module for testing Base class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

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
        self.assertEqual(len(json_data), 53)

    def test_for_rectangle_2_dicts(self):
        """Testing this function with class square
        """
        r1 = Rectangle(4, 7, 6, 5).to_dictionary()
        r2 = Rectangle(5, 5, 5, 5).to_dictionary()
        json_data = Base.to_json_string([r1, r2])
        self.assertEqual(str, type(json_data))
        self.assertEqual(len(json_data), 106)

    def test_one_sq(self):
        """Testing one square"""
        s1 = Square(2, 3, 5)
        list_of_objs = [s1]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        TrueFalse = os.path.exists(f'{list_of_objs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_one_sq_len(self):
        """Testing 1 square length"""
        s1 = Square(2, 3, 5)
        list_of_objs = [s1]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        filename = f'{list_of_objs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 39)

    def test_for_one_rec(self):
        """Testing for normal list"""
        r1 = Rectangle(2, 3, 5)
        list_of_objs = [r1]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        TrueFalse = os.path.exists(f'{list_of_objs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_one_rec_len(self):
        """Testing for normal test"""
        r1 = Rectangle(2, 3, 5)
        list_of_objs = [r1]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        filename = f'{list_of_objs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 53)

    def test_for_2Squares_list(self):
        """Testing for normal list"""
        sq1 = Square(2, 3, 5)
        sq2 = Square(4, 10, 1)
        list_of_objs = [sq1, sq2]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        TrueFalse = os.path.exists(f'{list_of_objs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_2Squares_list_len(self):
        """Testing for normal list"""
        sq1 = Square(2, 3, 5)
        sq2 = Square(4, 10, 1)
        list_of_objs = [sq1, sq2]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        filename = f'{list_of_objs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 79)

    def test_for_2Rectangle_list(self):
        """Testing for normal list"""
        r1 = Rectangle(2, 3, 5)
        r2 = Rectangle(4, 10, 1)
        list_of_objs = [r1, r2]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        TrueFalse = os.path.exists(f'{list_of_objs[0].__class__.__name__}.json')
        self.assertTrue(TrueFalse)

    def test_for_2Rectangle_listt(self):
        """Testing for normal listt"""
        r1 = Rectangle(2, 3, 5)
        r2 = Rectangle(4, 10, 1)
        list_of_objs = [r1, r2]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        filename = f'{list_of_objs[0].__class__.__name__}.json'
        with open(filename, 'r', encoding="UTF-8") as f:
            content = f.read()
            self.assertEqual(len(content), 105)

    def test_for_right_content(self):
        """Make sure that the file has the right content"""
        s1 = Square(2, 3, 5)
        s2 = Square(4, 10, 1)
        list_of_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        list_of_objs = [s1, s2]
        list_of_objs[0].__class__.save_to_file(list_of_objs)
        with open(f'{list_of_objs[0].__class__.__name__}.json', 'r') as f:
            content = f.read()
            self.assertEqual(content == Base.to_json_string(list_of_dicts), True)

    def test_for_None_s(self):
        """Test by None"""
        Base.save_to_file(None)
        if os.path.exists('Base.json'):
            with open('Base.json') as f:
                content = f.read()
        self.assertEqual(content, '[]')

    def test_for_empty_list_s(self):
        """Testing for empty list"""
        Base.save_to_file([])
        if os.path.exists('Base.json'):
            with open('Base.json') as f:
                content = f.read()
        self.assertEqual(content, '[]')

    def test_square_one(self):
        """Testing square one"""
        json_str = Base.to_json_string([{'size': 9, 'id': 1, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )

    def test_rectangle_one(self):
        """Testing rectangle one"""
        json_str = Base.to_json_string([{'size': 9, 'id': 1, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )

    def test_square_two(self):
        """Testing square two"""
        json_str = Base.to_json_string(
            [{'size': 9, 'id': 1, 'x': 1, 'y': 0},
             {'size': 10, 'id': 12, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 4)
        self.assertEqual(len(Base.from_json_string(json_str)[1]), 4)
        self.assertEqual(
            type(Base.from_json_string(json_str)[0]).__name__, 'dict'
        )
        self.assertEqual(
            type(Base.from_json_string(json_str)[1]).__name__, 'dict'
        )

    def test_rectangle_two(self):
        """Tesing square two"""
        json_str = Base.to_json_string(
            [{'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0},
             {'weight': 10, 'width': 9, 'id': 12, 'x': 1, 'y': 0}])
        self.assertEqual(len(Base.from_json_string(json_str)[0]), 5)
        self.assertEqual(len(Base.from_json_string(json_str)[1]), 5)
        self.assertEqual(type(
            Base.from_json_string(json_str)[0]
            ).__name__, 'dict')
        self.assertEqual(
            type(Base.from_json_string(json_str)[1]).__name__, 'dict')

    def test_for_None(self):
        """Tests for none"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_by_one_dict_rectangle_new(self):
        """Test for rectangle dict"""
        r1 = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Rectangle(10, 9, 1, 0, 1)
        d1 = Rectangle.create(**r1).to_dictionary()
        d2 = rec_obj.to_dictionary()
        self.assertEqual(d1, d2)

    def test_by_one_dict_rectangle_same_obj(self):
        """Test for rectangle dict"""
        r1 = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        newly_created = Rectangle.create(**r1)
        strr = str(newly_created)
        self.assertEqual("[Rectangle] (1) 1/0 - 10/9", strr)

    def test_by_one_dict_square_new(self):
        """Test for square dict"""
        s1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        d1 = Square.create(**s1).to_dictionary()
        d2 = rec_obj.to_dictionary()
        self.assertEqual(d1, d2)

    def test_by_one_dict_square_str_same_obj(self):
        """Test for rectangle dict"""
        s1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        newly_created = Square.create(**s1)
        strr = str(newly_created)
        self.assertEqual("[Square] (1) 1/0 - 10", strr)

    def test_square_will_not_equal(self):
        """Test square will not equal"""
        s1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**s1)
        self.assertNotEqual(rec_obj, new_obj)

    def test_rectangle_will_not_equal(self):
        """Test square will not equal"""
        rec = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**rec)
        self.assertNotEqual(rec_obj, new_obj)

    def test_square_will_not_is(self):
        """Test square will not equal"""
        s1 = {'size': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**s1)
        self.assertIsNot(rec_obj, new_obj)

    def test_rectangle_will_not_is(self):
        """Test square will not equal"""
        rec = {'height': 9, 'width': 10, 'id': 1, 'x': 1, 'y': 0}
        rec_obj = Square(10, 1, 0, 1)
        new_obj = Square.create(**rec)
        self.assertIsNot(rec_obj, new_obj)

    def test_square_normal_input(self):
        """Test square normal input"""
        List = Square.load_from_file()
        self.assertTrue(type(List) is list)

    def test_rectangle_normal_input(self):
        """Test square normal input"""
        List = Rectangle.load_from_file()
        self.assertTrue(type(List) is list)

    def test_for_objs_itself_rec(self):
        """Test for objs itself rec"""
        List = Rectangle.load_from_file()
        for obj in List:
            self.assertEqual(type(obj), Rectangle)

    def test_for_objs_itself_square(self):
        """Test for objs itself rec"""
        List = Square.load_from_file()
        for obj in List:
            self.assertEqual(type(obj), Square)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
