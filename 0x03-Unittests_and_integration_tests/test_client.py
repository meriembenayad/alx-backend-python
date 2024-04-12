#!/usr/bin/env python3
""" 4. Parameterize and patch as decorators """
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_get: Mock) -> None:
        """ Method to unit-test GithubOrgClient._public_repos_url """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_get.return_value = payload
        # create an instance of GitHubOrgClient
        client = GithubOrgClient("google")
        # Call the public_repos_url method
        pub_repos = client._public_repos_url

        # Assert (Check the result is as expected)
        self.assertEqual(
            pub_repos, payload['repos_url'])
