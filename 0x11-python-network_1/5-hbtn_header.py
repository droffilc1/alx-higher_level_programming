#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(dict(r.headers).get("X-Request-Id"))
