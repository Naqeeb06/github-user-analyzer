import github_api

user_input = input("Enter the GitHub username you want to analyze: ")
response = github_api.get_user(user_input)
print(response)
