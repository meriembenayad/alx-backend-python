#!/usr/bin/env python3
""" 4. Parameterize and patch as decorators """
from client import GithubOrgClient
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test case class """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"

        # Test that get_json was called once with expected arg
        mock_get.assert_called_once_with(url)
