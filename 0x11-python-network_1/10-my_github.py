#!/usr/bin/python3
"""Display Github ID using Github API"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(argv[2]),
               "X-GitHub-Api-Version": "2022-11-28"}

    res = requests.get(url, headers=headers)

    try:
        res.raise_for_status()
        json = res.json()
        print(json.get('id'))
    except requests.exceptions.JSONDecodeError:
        print(None)
    except requests.exceptions.HTTPError:
        print(None)
