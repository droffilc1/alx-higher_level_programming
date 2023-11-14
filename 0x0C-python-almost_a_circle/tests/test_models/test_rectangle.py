""" test_rectangle """


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Rectangle class."""

    def test_init_without_id(self):
        """Test init method without id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id + 1, r2.id)

    def test_init_with_id(self):
        """Test init method with id."""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_types(self):
        """Make sure type errors are raised when necessary"""
        with self.assertRaises(TypeError,
                               msg="height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaises(TypeError,
                               msg="width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaises(TypeError,
                                msg="x must be an integer"):
            Rectangle(10, 2, [], 3)

    def test_values(self):
        """Make sure value errors are raised when necessary"""
        with self.assertRaises(ValueError,
                               msg="width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError,
                               msg="y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_str_method(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        result = str(r1)
        expected_result = (
            f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - "
            f"{r1.width}/{r1.height}"
        )
        self.assertEqual(result, expected_result)

    def test_area(self):
        """Test area"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r1.area(), 6)
        self.assertAlmostEqual(r2.area(), 20)
        self.assertAlmostEqual(r3.area(), 56)


    def test_update_args(self):
        """Test update method with positional arguments"""
        r1 = Rectangle(4, 2, 1, 1, 1)
        r1.update(2, 3, 4, 5, 6)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        r1 = Rectangle(4, 2, 1, 1, 1)
        r1.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_update_mix_args_kwargs(self):
        """Tests update method with a mix of args and kwargs"""
        r1 = Rectangle(4, 2, 1, 1, 1)
        r1.update(2, height=4, y=6)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 6)

    def test_update_no_args_kwargs(self):
        """Tests update method with no args or kwargs"""
        r1 = Rectangle(4, 2, 1, 1, 1)
        r1.update()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

    def test_update_args_overflow(self):
        """Tests update method with too many positional arguments"""
        r1 = Rectangle(4, 2, 1, 1, 1)
        r1.update(2, 3, 4, 5, 6, 7)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_to_dictionary(self):
        """Test dictionary format"""
        r1 = Rectangle(x=1, y=9, id=1, height=2, width=10)
        expected_result = {
            'x': 1,
            'y': 9,
            'id': 1,
            'height': 2,
            'width': 10
        }

        self.assertEqual(r1.to_dictionary(), expected_result)


if __name__ == "__main__":
    unittest.main()
