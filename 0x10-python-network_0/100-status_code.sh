#!/bin/bash
#  displays only the status code of a response using curl
curl -so /dev/null -w "%{http_code}" "$1"
