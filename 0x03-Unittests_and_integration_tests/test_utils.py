#!/usr/bin/env python3
""" 0. Parameterize a unit test """
import unittest
from utils import access_nested_map, get_json, memoize
from typing import Dict, Any, Tuple
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ 0. Test case for the access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], expected: Any) -> None:
        """
            0. Test Method that uses the parameterized.expand decorator
            to test the access_nested_map function with different inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: Tuple[str]) -> None:
        """
            1. Test Method to test access_nested_map function
            using decorator @parameterized.expand with different inputs
            that should raise a KeyError
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ 2. Test case for test get_json Method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any], mock_get: Mock) -> None:
        """ 2. Test method to test get_json method """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ 3. Test case for test memoize method """

    def test_memoize(self) -> None:
        """ 3. Test memoize method """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        class_obj = TestClass()

        # Mock a_method of class_obj
        with patch.object(class_obj, 'a_method',
                          return_value=42) as mock_method:
            # Call a_property twice
            call_one = class_obj.a_property
            call_two = class_obj.a_property

            # Assert that the correct call is returned
            self.assertEqual(call_one, 42)
            self.assertEqual(call_two, 42)

            # Assert a_method is only called once
            mock_method.assert_called_once()
