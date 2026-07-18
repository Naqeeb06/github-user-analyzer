import github_api
import analyzer
import ui
from requests.exceptions import HTTPError

while True:
    user_input = input("\nEnter the GitHub username you want to analyze: ")

    if not user_input.strip():
        print("\nUsername cannot be empty")
        continue
    break
try:
    response = github_api.get_user(user_input)
    ui.display_user(response)
except HTTPError as e:
    status_code = e.response.status_code
    if status_code == 404:
        print(f"GitHub user '{user_input}' was not found.")
    elif status_code == 403:
        print(
            "GitHub API access was denied or the rate limit has been exceeded.Please try again later."
        )
    else:
        print(f"GitHub API returned an error '{status_code}'")

user_repos = github_api.get_repositories(user_input)
top_repos = analyzer.analyze_repositories(user_repos)
ui.display_top_repos(top_repos)

stats = analyzer.analyze_statistics(user_repos)
ui.display_statistics(stats)

language = input("Enter language: ")
filtered_repos = analyzer.filter_by_language(user_repos, language)
if not filtered_repos:
    print(f"No avaiable repositories for language: '{language}'")
else:
    ui.display_top_repos(filtered_repos)