#!/usr/bin/env python3
"""
Module containing unit tests for the client module.
This module uses the unittest framework to test GithubOrgClient.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict, Any
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Tests the public_repos method to ensure it returns the correct list
        of repositories and that mocked methods are called exactly once.
        """
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = mock_url

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])

            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(mock_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Any], license_key: str,
                         expected: bool) -> None:
        """
        Tests the has_license method to ensure it correctly identifies
        if a repository has a specific license.
        """
        client = GithubOrgClient("google")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Defines integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up class-level mocks for external requests before any
        tests in this class are run.
        """
        def get_payload(url: str) -> Mock:
            """Simulates requests.get().json() based on the URL."""
            mock_response = Mock()
            if url.endswith("repos"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = cls.org_payload
            return mock_response

        cls.get_patcher = patch('requests.get', side_effect=get_payload)

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stops the class-level patcher after all tests have run.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Integration test to verify that public_repos returns the
        expected list of repositories based on the loaded fixtures.
        """
        client = GithubOrgClient("google")

        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Integration test to verify that public_repos filters and returns
        the expected list of repositories when given a specific license.
        """
        client = GithubOrgClient("google")

        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
