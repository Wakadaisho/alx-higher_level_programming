#!/usr/bin/python3
"""Display 10 recents commits from a Github repo"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    params = {"per_page": 10, "page": 1}
    headers = {'Accept': 'application/vnd.github+json',
               "X-GitHub-Api-Version": "2022-11-28"}

    res = requests.get(url, params=params, headers=headers)

    try:
        res.raise_for_status()
        json = res.json()
        for r in json:
            print("{}: {}".format(
                r.get('sha'),
                r.get('commit').get('author').get('name'))
                  )
    except requests.JSONDecodeError as e:
        print("Not a valid JSON")
    except requests.HTTPError as e:
        print(None)
