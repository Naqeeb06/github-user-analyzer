import requests

BASE_URL = "https://api.github.com"

def get_user(username):
    url = f"{BASE_URL}/users/{username}"

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    user_data = response.json()
    user_info = {
        "name": user_data["name"], 
        "username" : user_data["login"], 
        "bio" : user_data["bio"], 
        "public_repositories" : user_data["public_repos"], 
        "followers" : user_data["followers"], 
        "following" : user_data["following"], 
        "account_created" : user_data["created_at"], 
        "location" : user_data["location"], 
        "company" : user_data["company"]
    }

    return user_info