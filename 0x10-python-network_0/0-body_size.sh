#!/usr/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
URL="$1"
curl -sI "$URL" | wc -c
