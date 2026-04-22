#!/usr/bin/env python3
"""
Module containing unit tests for the client module.
This module uses the unittest framework to test GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Defines test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Tests the org property of GithubOrgClient.
        Verifies that get_json is called exactly once with the correct URL,
        and that the property returns the expected payload.
        """
        mock_payload = {"login": org_name}
        mock_get_json.return_value = mock_payload

        client = GithubOrgClient(org_name)

        result = client.org

        self.assertEqual(result, mock_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """
        Tests the _public_repos_url property to ensure it returns
        the correct URL based on the mocked org payload.
        """
        known_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = known_payload

            client = GithubOrgClient("google")

            result = client._public_repos_url

            self.assertEqual(result, known_payload["repos_url"])
