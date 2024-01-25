#!/bin/bash
# displays the body of the response of a curl POST request with json
curl -sX POST -H "Content-type: application/json" -d @"$2" "$1"
