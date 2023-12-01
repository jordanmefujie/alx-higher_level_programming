#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': q})
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
