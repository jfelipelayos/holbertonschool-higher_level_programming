#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) < 2:
        data = ""
    else:
        data = sys.argv[1]

    req = requests.post("http://0.0.0.0:5000/search_user", data)
    try:

        if len(req.json()) != 0:
            print("[{}] {}".format(dict["id"], dict["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
