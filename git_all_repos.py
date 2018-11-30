import sys
import os
import requests


def get_total_repos(group, name,github_token=""):
    repo_urls = []
    page = 1
    while True:
        if github_token =="":
            url = 'https://api.github.com/{0}/{1}/repos?per_page=100&page={2}'
            r = requests.get(url.format(group, name, page))
        else:
            url = 'https://api.github.com/{0}/{1}/repos?per_page=100&page={2}&access_token={3}'
            r = requests.get(url.format(group, name, page,github_token))
            
        if r.status_code == 200:
            rdata = r.json()
            for repo in rdata:
                repo_urls.append(repo['clone_url'])
            if (len(rdata) >= 100):
                page = page + 1
            else:
                print('Found {0} repos.'.format(len(repo_urls)))
                break
        else:
            print(r)
            return False
    return repo_urls


def clone_repos(all_repos):
    print('Cloning...')
    counter = 1 
    total = str(len(all_repos))
    for repo in all_repos:
        print ('\nRepository ' + str(counter) + ' of ' + total + '\n' )
        os.system('git clone ' + repo)
        counter = counter + 1

if __name__ == '__main__':
    if len(sys.argv) > 3:
        total = get_total_repos(sys.argv[1], sys.argv[2],sys.argv[3])
        if total:
            clone_repos(total)
    if len(sys.argv) > 2:
        total = get_total_repos(sys.argv[1], sys.argv[2])
        if total:
            clone_repos(total)
    else:
        print('Usage: python USERS_OR_ORG GITHUB_USER_OR_ORG-NAME [GIT_TOKEN]')
