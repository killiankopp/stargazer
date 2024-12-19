import requests

from src.config import GH_BASE_URL, GH_HEADERS
from src.utils import extract_field


class GitHubAPI:
    @staticmethod
    def api_call(endpoint):
        url = f"{GH_BASE_URL}/{endpoint}"
        response = requests.get(url, headers = GH_HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def get_stargazers(user, repo):
        endpoint = f"repos/{user}/{repo}/stargazers"
        return GitHubAPI.api_call(endpoint)

    @staticmethod
    def list_stargazers(user, repo):
        datas = GitHubAPI.get_stargazers(user, repo)
        return extract_field(datas, 'login')

    @staticmethod
    def get_repo_starred(user):
        endpoint = f"users/{user}/starred"
        return GitHubAPI.api_call(endpoint)

    @staticmethod
    def list_repo_starred(user):
        datas = GitHubAPI.get_repo_starred(user)
        return extract_field(datas, 'full_name')
