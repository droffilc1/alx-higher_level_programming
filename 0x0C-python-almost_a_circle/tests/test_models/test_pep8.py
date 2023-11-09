#!/usr/bin/pyhton3
""" test_pep8 """

import unittest
import pycodestyle


class TestPycodestyle(unittest.TestCase):
    """Test for PEP-8"""

    def test_pep8(self):
        """Test for PEP-8"""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models'])
        self.assertEqual(result.total_errors, 0,
                         "Found pycodestyle errors.")
        print(result)
