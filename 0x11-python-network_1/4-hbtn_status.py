#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    r = r.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
