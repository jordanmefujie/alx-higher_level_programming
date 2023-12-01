x11. Python - Network #1
Python
Scripting
Back-end
API

Resources
Read or watch:

HOWTO Fetch Internet Resources Using urllib Package
Quickstart with Requests package
Requests package
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)


1. fetches https://intranet.hbtn.io/status, not allowed to import any packages other than urllib

2. takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response

3. takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

4. takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)

5. fetches https://intranet.hbtn.io/status, not allow to import packages other than requests

6. takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

7. takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response

8. takes in a URL, sends a request to the URL and displays the body of the response

9. takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter

10. takes in a string and sends a search request to the Star Wars API

11. takes your Github credentials (username and password) and uses the Github API to display your id

