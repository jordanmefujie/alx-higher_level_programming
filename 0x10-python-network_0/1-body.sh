#!/bin/bash

# Check if URL is provided as an argument
curl -s -w "%{http_code}" "$1" | awk 'END {if ($0 == 200) print ""; else print $0}'
