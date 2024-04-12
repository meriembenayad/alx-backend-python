#!/usr/bin/env python3
""" 0. Parameterize a unit test """
import unittest
from utils import access_nested_map
from typing import Dict, Any, Tuple
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Test case for the access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], expected: Any) -> None:
        """ Test Method that uses the parameterized.expand decorator
            to test the access_nested_map function with different inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
