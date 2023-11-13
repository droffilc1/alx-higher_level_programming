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


if __name__ == "__main__":
    unittest.main()
