""" test_square """


import io
import sys
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

class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        """Test __str__ method print"""
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        """Test __str__ method size_x"""
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        """Test __str__ method size_x_y"""
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        """Test __str__ method size_x_y_id"""
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        """Test __str__ method changed attributtes"""
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        """Test __str__ method with one arg"""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_str_method(self):
        """Tests the __str__ method"""
        obj = Square(4, 2, 1, 1)
        expected_output = "[Square] (1) 2/1 - 4"
        self.assertEqual(str(obj), expected_output)
    
    def test_str_w(self):
        """Test __str__ method width"""
        s1 = Square(4)
        self.assertEqual(str(s1), "[Square] (67) 0/0 - 4")

    def test_str_w_x(self):
        """Test __str__ method w_x"""
        s1 = Square(1, 2)
        self.assertEqual(str(s1), "[Square] (68) 2/0 - 1")

    def test_str_w_x_y(self):
        """Test __str__ method w_x_y"""
        s1 = Square(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (69) 2/3 - 1")

    def test_strinf_rep_w_x_y_id(self):
        s1 = Square(1,2,3,4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    # Test display method
    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)

if __name__ == "__main__":
    unittest.main()
