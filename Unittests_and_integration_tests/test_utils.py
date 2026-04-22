#!/usr/bin/env python3
"""
Module containing unit tests for the utils module.
This module uses the unittest framework and parameterized testing.
"""
import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Defines test cases for the access_nested_map function from utils.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """
        Tests that access_nested_map correctly accesses values
        within nested dictionaries based on the provided path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: str) -> None:
        """
        Tests that access_nested_map raises a KeyError for missing keys
        and verifies the exception message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(expected, str(context.exception))
