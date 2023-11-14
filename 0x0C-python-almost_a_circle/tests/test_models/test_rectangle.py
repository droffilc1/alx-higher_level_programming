""" test_rectangle """

import io
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test Rectangle class."""

    def test_init_without_id(self):
        """Test init method without id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(1, 2)
        self.assertEqual(r1.id + 1, r2.id)
        self.assertEqual(r2.id + 1, r3.id)

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

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

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

    class test_width(unittest.TestCase):
        """testing width gettter
        """
    def test_basic(self):
        """Basic testing
        """
        obj = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(obj.width, 10)

    def test_negative_number(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(-10, 20, 30, 40, 50)

    def test_different_type_float(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(10.4, 20, 30, 40, 50)

    def test_different_type_str(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle("str", 20, 30, 40, 50)

    def test_different_type_bool(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(True, 20, 30, 40, 50)

    def test_different_type_iteratives(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle([10.4], 20, 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle((10.4, 9), 20, 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle({10.4, 9}, 20, 30, 40, 50)

    def test_for_zero(self):
        """Basic testing
        """
        with self.assertRaises(
            ValueError, msg='ValueError: width must be > 0'
        ):
            obj = Rectangle(0, 20, 30, 40, 50)

    def test_different_type_None(self):
        """Basic testing
        """
        with self.assertRaises(
            TypeError, msg='width must be an integer'
        ):
            obj = Rectangle(None, 20, 30, 40, 50)


class test_height(unittest.TestCase):
    """Testing height getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(obj.height, 20)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: height must be > 0'
        ):
            obj = Rectangle(10, -20, 30, 40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, 20.5, 30, 40, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, "str", 30, 40, 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, True, 30, 40, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, [20.4], 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, (20.4, 9), 30, 40, 50)
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, {20.4, 9}, 30, 40, 50)

    def test_for_zero(self):
        """Testing with zero value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: height must be > 0'
        ):
            obj = Rectangle(10, 0, 30, 40, 50)

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='height must be an integer'
        ):
            obj = Rectangle(10, None, 30, 40, 50)


class test_x(unittest.TestCase):
    """Testing x getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(obj.x, 30)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: x must be >= 0'
        ):
            obj = Rectangle(10, 20, -30, 40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, 30.5, 40, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, "str", 40, 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, True, 40, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, [30.4], 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, (30.4, 9), 40, 50)
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, {30.4, 9}, 40, 50)

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='x must be an integer'
        ):
            obj = Rectangle(10, 20, None, 40, 50)


class test_y(unittest.TestCase):
    """Testing y getter
    """
    def test_basic(self):
        """Basic testing
        """
        obj = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(obj.y, 40)

    def test_negative_number(self):
        """Testing with a negative value
        """
        with self.assertRaises(
            ValueError, msg='ValueError: y must be >= 0'
        ):
            obj = Rectangle(10, 20, 30, -40, 50)

    def test_different_type_float(self):
        """Testing with a float value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, 40.5, 50)

    def test_different_type_str(self):
        """Testing with a string value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, "str", 50)

    def test_different_type_bool(self):
        """Testing with a boolean value
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, True, 50)

    def test_different_type_iteratives(self):
        """Testing with iterable types
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, [40.4], 50)
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, (40.4, 9), 50)
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, {40.4, 9}, 50)

    def test_different_type_None(self):
        """Testing with None
        """
        with self.assertRaises(
            TypeError, msg='y must be an integer'
        ):
            obj = Rectangle(10, 20, 30, None, 50)

class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


if __name__ == "__main__":
    unittest.main()
