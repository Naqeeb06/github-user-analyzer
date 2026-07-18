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

def display_top_repos(top_repos):
    print("\n====================\nTop Repositories\n====================")
    for i, repo in enumerate(top_repos):
        print(f"\n===============\nRepository {i+1}:\n===============\n")
        print(f"Repository Name: {repo['repo_name']}")
        print(f"Stars: {repo['stars']}")

        if repo['language'] is None:
            print("Language: Not specified.")
        else:
            print(f"Language: {repo['language']} ")

        if repo['description'] is None:
            print("Description: Not specified.")
        else:
            print(f"Description: {repo['description']}")

def display_statistics(stats):
    print("\n====================\nUser Stats\n====================\n")
    print(f"Total Repositories:  {stats['total_repos']}")
    print(f"Total Stars: {stats['total_stars']}")       
    print(f"Average stars per repository: {stats['average_stars']}")

    if stats['most_used_language'] is None:
        print("Most used language: Not available")
    else:
        print(f"Most used language: {stats['most_used_language']}")

    