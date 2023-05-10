import os
from github import Github
import json

# Get required information from environment variables
token = os.environ['GITHUB_TOKEN']
repo_name = os.environ['GITHUB_REPOSITORY']
github_event_path = os.environ['GITHUB_EVENT_PATH']

# Load GitHub event data
with open(github_event_path, 'r') as f:
    github_event_data = json.load(f)

pr_number = github_event_data['pull_request']['number']
epic_branch_name = github_event_data['pull_request']['base']['ref']
pr_title = github_event_data['pull_request']['title']


# Authenticate with GitHub API
g = Github(token)
repo = g.get_repo(repo_name)

print(repo_name)
print("--------------------------------")
print(pr_number)
print("--------------------------------")
print(epic_branch_name)
print("--------------------------------")
print(pr_title)

# # Find the PR of the epic branch
# epic_pr = None
# for pr in repo.get_pulls(state='open'):
#     if pr.head.ref == epic_branch_name:
#         epic_pr = pr
#         break

# if epic_pr:
#     # Get current PR description
#     current_description = epic_pr.body

#     # Generate task PR link and append it to the description
#     task_pr_url = f"https://github.com/{repo_name}/pull/{pr_number}"
#     updated_description = f"{current_description}\n- [{pr_number}] {pr_title}: {task_pr_url}"

#     # Update the epic branch PR description
#     epic_pr.edit(body=updated_description)
# else:
#     print(f"No open PR found for the epic branch '{epic_branch_name}'.")
