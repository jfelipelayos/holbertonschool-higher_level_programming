#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit()
    path = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    commits = requests.get(path).json()
    for val in commits[:10]:
        sha = val["sha"]
        info = val["commit"]["author"]["name"]
        print("{}: {}".format(sha, info))
