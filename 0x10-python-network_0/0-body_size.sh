#!/bin/bash

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and display the size of the response body in bytes
response_size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')

if [ -z "$response_size" ]; then
    echo "Unable to retrieve response size."
else
    echo "Size of the response body: ${response_size} bytes"
fi
