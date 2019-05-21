#!/usr/bin/env python3

"""
open_prs.py lists all the open pull requests for the repositories provided in
`repos` for the users specified in `usernames`.
You have to have your Github API token in then environment variable
`GITHUB_TOKEN_GALAXY`.
"""

__author__ = "Jochen Breuer"
__email__  = "jbreuer@suse.de"
__license__ = "GPLv3"

import os
import requests
import sys

usernames = (
    "brejoc",
    "dincamihai",
    "meaksh",
)
repos = (
    "saltstack/salt",
    "openSUSE/salt",
    "cobbler/cobbler",
    "uyuni-project/uyuni",
)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_prs_for_user(username):
    query = """
    {
    user(login: "%s") {
        name
        login
        pullRequests(first: 100, states: OPEN) {
        totalCount
        nodes {
            repository {
            id
            nameWithOwner
            }
            createdAt
            number
            title
            url
        }
        pageInfo {
            hasNextPage
            endCursor
        }
        }
    }
    }
    """ % username
    url = 'https://api.github.com/graphql'
    json = { 'query' : query }
    api_token = os.environ.get('GITHUB_TOKEN_GALAXY')
    headers = {'Authorization': 'token %s' % api_token}

    r = requests.post(url=url, json=json, headers=headers)
    return r.json()


if __name__ == "__main__":
    for username in usernames:
        data = get_prs_for_user(username)
        print("{}{}{}".format(bcolors.OKBLUE, data['data']['user']['name'], bcolors.ENDC))
        print("=" * 80)
        pull_requests = data['data']['user']['pullRequests']['nodes']
        if len(pull_requests) == 0:
            print("No pull requests!")
        for i, pr in enumerate(pull_requests):
            title = pr['title']
            repo = pr['repository']['nameWithOwner']
            if repo not in repos:
                continue
            url = pr['url']
            print("{}{}{}".format(bcolors.OKGREEN, title, bcolors.ENDC))
            print("🔗 {}".format(url))
            if i+1 == len(pull_requests):
                print()
                print()
                continue
            print("-" * 80)