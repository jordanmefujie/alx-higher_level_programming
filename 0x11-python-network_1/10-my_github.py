#!/usr/bin/python3
"""
takes your GitHub credentials (username and personal access token) and
uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    takes your GitHub credentials (username and personal access token) and
    uses the GitHub API to display your id
    """
    if len(argv) != 3:
        print("Usage: ./script.py <username> <token>")
        exit(1)

    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Basic {username}:{token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        user_id = response.json().get('id')
        print(f"Your GitHub user id: {user_id}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Not a valid JSON response")
