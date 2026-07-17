def analyze_repositories(repos_list):
    sorted_repos = sorted(repos_list, key=lambda repo: repo['stars'], reverse= True)

    top_repos = sorted_repos[:3]

    return top_repos

def analyze_statistics(repos_list):
    #? total repositories
    total_repositories = len(repos_list)

    #? total stars
    total_stars = 0

    for repo in repos_list:
        total_stars += repo['stars']

    #? average stars
    if total_repositories == 0:
        average_stars = 0
    else:
        average_stars = total_stars / total_repositories

    stats = {
        'total_repos' : total_repositories,
        'total_stars' : total_stars,
        'average_stars' : average_stars
    }

    return stats