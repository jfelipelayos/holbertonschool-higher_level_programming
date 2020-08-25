#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
   with the email as a parameter, and displays the body of the response
   (decoded in utf-8)
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    req = request.Request(sys.argv[1], data.encode('ascii'))
    with request.urlopen(req) as response:
        body = response.read()
    print(body.decode("utf-8"))
