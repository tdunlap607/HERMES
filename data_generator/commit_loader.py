"""
The purpose of commit_loader is to provide functions to 
load the necessary data (e.g., commit message, commit patch, link data) for the model
"""
import data_generator.github_api as gr


def commit_info(repo_owner: str, repo_name: str, commit_sha: str) -> str:
    """Returns the commit message for a given commit within a GitHub project

    Args:
        repo_owner (str): The account owner of the repository.
        repo_name (str): The name of the repository.
        commit_sha (str): SHA for a target commit.

    Returns:
        _type_: _description_
    """
    
    commit_data = gr.commits(repo_owner=repo_owner, repo_name=repo_name, commit_sha=commit_sha)
    
    return commit_data