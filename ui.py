def display_user(user_info):
    print("\n====================\nGitHub User\n====================\n")
    print(f"Name: {user_info['name']}")
    print(f"Username: {user_info['username']}")

    if user_info['bio'] is None:
        print("Bio: Not specified.")
    else:
        print(f"Bio: {user_info['bio']}")

    print(f"\nPublic Repositories: {user_info['public_repositories']}")
    print(f"Followers: {user_info['followers']}")
    print(f"Following: {user_info['following']}")

    print("\n")
    if user_info['location'] is None:
        print("Location: Not specified.")
    else:
        print(f"Location: {user_info['location']}")

    if user_info['company'] is None:
        print("Company: Not specified.")
    else:
        print(f"Company: {user_info['company']}")

    print(f"\nAccount Created at: {user_info['account_created']}\n")