import requests

url="https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept" : "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f'Status Code: {response.status_code}')
response_dict = response.json()

print(f"Total Repo: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"\nOwner: {repo_dict['owner']['login']}")
    print(f"\nStars: {repo_dict['stargazers_count']}")
    print(f"\nRepository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")