import pytest
import responses

from src.config import GH_BASE_URL
from src.github_api import GitHubAPI


class TestGitHubAPI:
    @responses.activate
    def test_api_call_success(self):
        endpoint = "repos/toto/mySuperRepo/stargazers"
        url = f"{GH_BASE_URL}/{endpoint}"
        responses.add(
            responses.GET,
            url,
            json = [{"login": "user1"}, {"login": "user2"}],
            status = 200
        )

        result = GitHubAPI.api_call(endpoint)
        assert result == [{"login": "user1"}, {"login": "user2"}]

    @responses.activate
    def test_api_call_failure(self):
        endpoint = "repos/toto/mySuperRepo/stargazers"
        url = f"{GH_BASE_URL}/{endpoint}"
        responses.add(
            responses.GET,
            url,
            json = {"message": "Not Found"},
            status = 404
        )

        with pytest.raises(Exception) as excinfo:
            GitHubAPI.api_call(endpoint)

        assert "404 Client Error" in str(excinfo.value)

    def test_get_stargazers(self, monkeypatch):
        def mock_api_call(endpoint):
            return [{"login": "user1"}, {"login": "user2"}]

        monkeypatch.setattr(GitHubAPI, "api_call", mock_api_call)

        result = GitHubAPI.get_stargazers("toto", "mySuperRepo")
        assert result == [{"login": "user1"}, {"login": "user2"}]

    def test_list_stargazers(self, monkeypatch):
        def mock_get_stargazers(user, repo):
            return [{"login": "user1"}, {"login": "user2"}]

        def mock_extract_field(datas, field):
            return [data[field] for data in datas]

        monkeypatch.setattr(GitHubAPI, "get_stargazers", mock_get_stargazers)
        monkeypatch.setattr("src.utils.extract_field", mock_extract_field)

        result = GitHubAPI.list_stargazers("octocat", "Hello-World")

        assert result == ["user1", "user2"]

    def test_get_repo_starred(self, monkeypatch):
        def mock_api_call(endpoint):
            return [{"full_name": "user1/mySuperRepo"}, {"full_name": "user2/mySuperRepo"}]

        monkeypatch.setattr(GitHubAPI, "api_call", mock_api_call)

        result = GitHubAPI.get_repo_starred("toto")
        assert result == [{"full_name": "user1/mySuperRepo"}, {"full_name": "user2/mySuperRepo"}]

    def test_list_repo_starred(self, monkeypatch):
        def mock_get_repo_starred(user):
            return [{"full_name": "user1/mySuperRepo"}, {"full_name": "user2/mySuperRepo"}]

        def mock_extract_field(datas, field):
            return [data[field] for data in datas]

        monkeypatch.setattr(GitHubAPI, "get_repo_starred", mock_get_repo_starred)
        monkeypatch.setattr("src.utils.extract_field", mock_extract_field)

        result = GitHubAPI.list_repo_starred("toto")

        assert result == ["user1/mySuperRepo", "user2/mySuperRepo"]
