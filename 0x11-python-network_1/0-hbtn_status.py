#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body respose:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
