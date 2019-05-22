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
import sys
import requests
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from dateutil import parser

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
    "SUSE/spacewalk",
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


def get_prs_for_user(username, api_token):
    """\
    Fetches the pull requests for the given user and returns
    the data set as a dict.
    """
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
    headers = {'Authorization': 'token %s' % api_token}

    r = requests.post(url=url, json=json, headers=headers)
    return r.json()


def get_colour_coding_for_pr(pr, days=14):
    """\
    Returns the colour code needed to print to the CLI.
    The colour is green, unless the pr is > `days` old.
    """
    created_at = parser.parse(pr['createdAt'])
    now = datetime.now(timezone.utc)
    age = now - created_at
    colour = bcolors.OKGREEN
    if age > timedelta(days=days):
        colour = bcolors.FAIL
    return colour


def filter_prs_by_repos(pull_requests, repos):
    """\
    Returns only the pull requests that are listed in repos.
    """
    return [pull_request for pull_request in pull_requests if pull_request['repository']['nameWithOwner'] in repos]


if __name__ == "__main__":
    api_token = os.environ.get('GITHUB_TOKEN_GALAXY')
    if not api_token:
        sys.stderr.write("Please provide a Github API token via environment variable `GITHUB_TOKEN_GALAXY`.")
        sys.exit(1)
    for username in usernames:
        data = get_prs_for_user(username, api_token)
        print("{}{}{}".format(bcolors.OKBLUE, data['data']['user']['name'], bcolors.ENDC))
        print("=" * 80)
        pull_requests = filter_prs_by_repos(data['data']['user']['pullRequests']['nodes'], repos)
        if len(pull_requests) == 0:
            print("No pull requests!")
        for i, pr in enumerate(pull_requests):
            title = pr['title']
            repo = pr['repository']['nameWithOwner']
            if repo not in repos:
                continue
            url = pr['url']
            print("{}{}{}".format(get_colour_coding_for_pr(pr), title, bcolors.ENDC))
            print("🔗 {}".format(url))
            if i+1 == len(pull_requests):
                print("\n")
                continue
            print("-" * 80)
