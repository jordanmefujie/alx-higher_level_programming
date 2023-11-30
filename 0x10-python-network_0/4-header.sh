#!/bin/bash
# This takes in a URL as an argument, sends a GET request to the URL
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
