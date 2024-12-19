import json


def get_starneighbours(user, repo):
    response = [{"repo": "killiankopp/stargazer", "stargazers": ["user1", "user2"]},
                {"repo": "danielmiessler/fabric", "stargazers": ["user3", "user4"]}]

    return json.dumps(response)
