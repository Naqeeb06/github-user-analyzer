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

    language_count = {}

    for repo in repos_list:
        language = repo['language']
    
        if language is None:
            continue

        if language not in language_count:
            language_count[language] = 1
        else:
            language_count[language] += 1
    if language_count:
        most_used_language = max(language_count, key=lambda language: language_count[language])
    else:
        most_used_language = None

    stats = {
        'total_repos' : total_repositories,
        'total_stars' : total_stars,
        'average_stars' : average_stars,
        'most_used_language' : most_used_language
    }

    return stats

def filter_by_language(repos_list,language):
    filtered_repos = []

    for repo in repos_list:
        if repo['language'] is None:
            continue
        
        if repo['language'].lower() == language.lower():
            filtered_repos.append(repo)

    return filtered_repos