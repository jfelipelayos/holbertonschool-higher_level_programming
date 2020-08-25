#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
   the body of the response (decoded in utf-8).
"""
from urllib import request, parse, error
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            data = response.read()
        print(data.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
