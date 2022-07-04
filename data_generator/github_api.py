"""
Functions to handle GitHub interactions
"""

import requests

"""Set auth"""
token = ""
headers = {'Authorization': 'token %s' % token}


def commits(repo_owner: str, repo_name: str, commit_sha: str) -> dict:
    """Hits the commit API for a specific commit_sha.
    Info: https://docs.github.com/en/rest/commits/commits
    
    Args:
        repo_owner (str): The account owner of the repository.
        repo_name (str): The name of the repository.
        commit_sha (str): SHA for a target commit.

    Returns:
        dict: Full commit info, so end-user can do whatever they desire
    """
    #TODO: Build funcitonality for Authorization if desired
    # token = ""
    # headers = {'Authorization': 'token %s' % token}
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}"
    
    response = requests.get(url)
    response.close()
    
    return response.json()