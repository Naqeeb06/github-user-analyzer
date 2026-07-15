import github_api
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
        print("GitHub API access was denied or the rate limit has been exceeded.Please try again later.")
    else:
        print(f"GitHub API returned an error '{status_code}'")