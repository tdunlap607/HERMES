"""
Simple test file for functionality within the data_generator helpers
"""
import commit_loader as cl

if __name__ == '__main__':
    """Set sample GitHub project with a target commit"""
    repo_owner = "bcgit"
    repo_name = "bc-java"
    commit_sha =  "df0ef076d9ddb064b76e135a9b9d512634680c6b"
    
    commit_data = cl.commit_info(repo_owner=repo_owner,
                                 repo_name=repo_name,
                                 commit_sha=commit_sha)
    
    print("breakpoint")