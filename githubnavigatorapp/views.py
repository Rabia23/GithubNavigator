import requests

from datetime import datetime
from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    """
    queries the github api based on the search_term to get repositories with some
    information about latest commit in the repository from the first page of search
    result.

    Example Requests:

        GET api.github.com/search/repositories?q={search_term}+in:name&page=1

        GET api.github.com/repos/{owner}/{repo}/commits

    Returns:
            A list of first 5 (newest) repositories.
    """
    search_term = request.GET.get('search_term', None)
    if search_term:
        payload = {"q": "{} in:name".format(search_term), "page": "1"}
        repos_req = requests.get('https://api.github.com/search/repositories', params=payload)

        # sorting repositories by created_at in descending order
        sorted_repos = sorted(repos_req.json()['items'], key=lambda x: x['created_at'], reverse=True)

        repos_data = []
        for position, repository in enumerate(sorted_repos[:5]):
            item = {
                'position': position + 1,
                'name': repository['name'],
                'created_at': datetime.strptime(repository['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                'owner_name': repository['owner']['login'],
                'owner_url': repository['owner']['html_url'],
                'owner_avatar_url': repository['owner']['avatar_url']
            }
            # get the commits of the given repository
            commits_req = requests.get(repository['commits_url'].replace('{/sha}', ''))
            if commits_req.json():
                last_commit = commits_req.json()[0]
                item['last_commit'] = {
                    'sha': last_commit['sha'],
                    'message': last_commit['commit']['message'],
                    'author_name': last_commit['commit']['author']['name']
                }

            repos_data.append(item)

        context = {'search_term': search_term, 'repos_data': repos_data}
        return render(request, 'template.html', context)
    else:
        return HttpResponseNotFound('<h1>No Page Found</h1>')
