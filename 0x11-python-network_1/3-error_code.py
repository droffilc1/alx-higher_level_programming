#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
    except urllib.error.HTTPError as e:
        print("Error code: {e.code}")
