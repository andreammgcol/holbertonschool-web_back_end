#!/usr/bin/env python3
""" Test module """

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """The method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class
    """
    @parameterized.expand([
         ("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Method that test utils.get_json"""
        mock = Mock()
        mock.json.return_value = test_payload

        with patch('requests.get', return_value=mock):
            my_json = get_json(test_url)
            self.assertEqual(my_json, test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """TestMemoize class
    """
    def test_memoize(self):
        """ Method test_memoize """
        class TestClass:
            """TestClass class
            """
            def a_method(self):
                """ Return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Return a_method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock.assert_called_once()
