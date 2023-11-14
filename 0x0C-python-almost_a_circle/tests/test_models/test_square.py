""" test_square """

import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """Tests for class Square."""
    def test_area_1_arg(self):
        """Test area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_area_more_args(self):
        """Test are with more arguments"""
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_str_method(self):
        """Test __str__ method"""
        s1 = Square(5)
        result = str(s1)
        expected_result = f"[Square] ({s1.id}) {s1.x}/{s1.y} - {s1.size}"
        self.assertEqual(result, expected_result)

    def test_size(self):
        """Test for size"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_update_args(self):
        """Test update method with positional arguments"""
        s1 = Square(5)
        s1.update(1, 2, 2, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 4)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        s1 = Square(4, 2, 1, 1)
        s1.update(id=2, x=3, y=4, size=5)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_update_mix_args_kwargs(self):
        """Tests update method with a mix of args and kwargs"""
        s1 = Square(4, 2, 1, 1)
        s1.update(2, size=4, y=6)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 6)

    def test_update_no_args_kwargs(self):
        """Tests update method with no args or kwargs"""
        s1 = Square(4, 2, 1, 1)
        s1.update()
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 1)

    def test_update_args_overflow(self):
        """Tests update method with too many positional arguments"""
        s1 = Square(4, 2, 1, 1)
        s1.update(2, 3, 4, 5, 6, 7)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)

    def test_to_dictionary(self):
        """Test dictionary format"""
        s1 = Square(id=1, x=2, y=1, size=10)
        expected_result = {
            'x': 2,
            'y': 1,
            'id': 1,
            'size': 10,
        }

        self.assertEqual(s1.to_dictionary(), expected_result)

class test_size(unittest.TestCase):
    """testing width gettter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.size, 10)

    def test_negative_number(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Square(-10, 30, 40, 50)

    def test_different_type_float(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square(10.4, 30, 40, 50)

    def test_different_type_str(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square("str", 30, 40, 50)

    def test_different_type_bool(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square(True, 30, 40, 50)

    def test_different_type_iteratives(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square([10.4], 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square((10.4, 9), 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Square({10.4, 9}, 30, 40, 50)

    def test_for_zero(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(0, 30, 40, 50)

    def test_different_type_None(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(None, 30, 40, 50)


class test_x(unittest.TestCase):
    """Testing x getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.x, 30)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: x must be >= 0'
        ):
            obj = Square(10, -30, 40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, 30.5, 40, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, "str", 40, 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, True, 40, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, [30.4], 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, (30.4, 9), 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, {30.4, 9}, 40, 50)

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Square(10, None, 40, 50)


class test_y(unittest.TestCase):
    """Testing y getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Square(10, 30, 40, 50)
        self.assertEqual(obj.y, 40)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: y must be >= 0'
        ):
            obj = Square(10, 30, -40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, 40.5, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, "str", 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, True, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, [40.4])
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, (40.4, 9))
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, {40.4, 9})

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Square(10, 30, None)

if __name__ == "__main__":
    unittest.main()
