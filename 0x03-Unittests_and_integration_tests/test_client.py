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
        4. Test that GithubOrgClient.org returns the correct value
        """
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"

        # Test that get_json was called once with expected arg
        mock_get.assert_called_once_with(url)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_get: Mock) -> None:
        """ 5. Method to unit-test GithubOrgClient._public_repos_url """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_get.return_value = payload
        # create an instance of GitHubOrgClient
        client = GithubOrgClient("google")
        # Call the public_repos_url method
        pub_repos = client._public_repos_url

        # Assert (Check the result is as expected)
        self.assertEqual(
            pub_repos, payload['repos_url'])

    @patch("client.get_json", return_value=[{"name": "repos_one"},
                                            {"name": "repos_two"}])
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """ 6. Method to test GithubOrgClient.public_repos """
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_pub_repos_url:
            mock_pub_repos_url.return_value = (
                'https://api.github.com/orgs/google/repos'
            )
            github_url_client = GithubOrgClient('google')
            self.assertEqual(github_url_client.public_repos(),
                             ["repos_one", "repos_two"])
            mock_get_json.assert_called_once()
            mock_pub_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_licence(self, repo, license_key, expected_result) -> None:
        """ unit-test GithubOrgClient.has_license """
        github_client_url = GithubOrgClient('google')
        self.assertEqual(github_client_url.has_license(
            repo, license_key), expected_result)
