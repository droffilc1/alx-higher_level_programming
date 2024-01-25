#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl $1 -sX OPTIONS | grep Allow | cut -d ' ' -f2-
