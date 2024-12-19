import os

GH_BASE_URL = "https://api.github.com"
GH_API_VERSION = "2022-11-28"
GH_TOKEN = os.getenv('GH_TOKEN')
GH_HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GH_TOKEN}",
    "X-GitHub-Api-Version": f"{GH_API_VERSION}"
}
