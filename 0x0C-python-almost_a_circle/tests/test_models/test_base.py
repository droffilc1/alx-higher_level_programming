"""A module for testing Base class."""

import unittest
from models.base import Base

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


if __name__ == "__main__":
    unittest.main()
