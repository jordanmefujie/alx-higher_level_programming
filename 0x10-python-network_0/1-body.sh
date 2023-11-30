#!/bin/bash

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request and display the body if the status code is 200
response=$(curl -s -w "%{http_code}" "$url")

# Extract the status code from the response
status_code=$(tail -c 3 <<< "$response")

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
    # Extract and display the body of the response
    body=$(sed '$s/^[ \t]*//' <<< "${response%"$status_code"}")
    echo "Response Body: $body"
else
    echo "Error: Non-200 status code received - $status_code"
fi
