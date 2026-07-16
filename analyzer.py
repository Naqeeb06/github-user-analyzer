def analyze_repositories(repos_list):
    sorted_repos = sorted(repos_list, key=lambda repo: repo['stars'], reverse= True)

    top_repos = sorted_repos[:3]

    return top_repos