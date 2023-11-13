""" test_square """

import unittest
from models.square import Square


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
        s1 = Square(id=None, x=0, y=0, size=0)
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

if __name__ == "__main__":
    unittest.main()
