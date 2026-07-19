import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
if not TOKEN:
    raise ValueError("GitHub token not found. Please configure your .env file.")

HEADERS = {
    "Authorization" : f"Bearer {TOKEN}"
}

BASE_URL = "https://api.github.com"

def get_user(username):
    url = f"{BASE_URL}/users/{username}"

    response = requests.get(url, headers= HEADERS, timeout=5)
    response.raise_for_status()
    user_data = response.json()
    created_at = datetime.strptime(user_data['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = created_at.strftime("%B %d, %Y")
    user_info = {
        "name": user_data["name"], 
        "username" : user_data["login"], 
        "bio" : user_data["bio"], 
        "public_repositories" : user_data["public_repos"], 
        "followers" : user_data["followers"], 
        "following" : user_data["following"], 
        "account_created" : formatted_date, 
        "location" : user_data["location"], 
        "company" : user_data["company"]
    }

    return user_info

def get_repositories(username):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    repositories_data = response.json()

    repos_list = []
    for repo in repositories_data:
        repository_info = {
            "repo_name" : repo['name'],
            "stars" : repo['stargazers_count'],
            "language" : repo['language'],
            "description" : repo['description']
            }

        repos_list.append(repository_info)
        
    return repos_list