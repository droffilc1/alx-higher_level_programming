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
        """Test for different types"""
        with self.assertRaises(TypeError,
                               msg="height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaises(TypeError, 
                               msg="width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaises(ValueError, 
                               msg="width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError, 
                                msg="x must be an integer"):
            Rectangle(10, 2, [], 3)
        with self.assertRaises(ValueError, 
                               msg="y must be >= 0"):
            Rectangle(10, 2, 3, -1)

if __name__ == "__main__":
    unittest.main()
