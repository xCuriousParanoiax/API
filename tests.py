import json
import requests


# Step 1

# We try comparing files before logging in and we get "Not authenticated":

files = {
    'file1': ('img.jpeg', open('img.jpeg', 'rb')),
    'file2': ('img3.jpeg', open('img3.jpeg', 'rb')),
}

compare_response = requests.post('http://localhost:8000/compare/', files=files)

json_compare_response = json.loads(compare_response.text)

print(json_compare_response["detail"])










# Step 2

# We log in and try comparing files without using the token and we get "Not authenticated":

data = {
  'username': 'johndoe',
  'password': 'secret',
}

files = {
    'file1': ('img.jpeg', open('img.jpeg', 'rb')),
    'file2': ('img3.jpeg', open('img3.jpeg', 'rb')),
}

login_response = requests.post('http://localhost:8000/token/', data=data)
compare_response = requests.post('http://localhost:8000/compare/', files=files)

json_compare_response = json.loads(compare_response.text)

print(json_compare_response["detail"])










# Step 3

# We log in and get the token then make a request using the token and it works:

data = {
  'username': 'johndoe',
  'password': 'secret',
}

login_response = requests.post('http://localhost:8000/token/', data=data)

json_login_response = json.loads(login_response.text)


token = f'{json_login_response["token_type"]} {json_login_response["access_token"]}'

headers = {
    'Authorization': token
}

files = {
    'file1': ('img.jpeg', open('img.jpeg', 'rb')),
    'file2': ('img3.jpeg', open('img3.jpeg', 'rb')),
}

compare_response = requests.post('http://localhost:8000/compare/', headers=headers, files=files)

json_compare_response = json.loads(compare_response.text)

print(json_compare_response["similarity-percentage"])










# Step 4

# We turn off, then turn on the server and make a request using the token without logging in (token doesn't expire) and it works:

token = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIn0.adqb-sj6G4xl7w7t9A4oRUBf1jNmcrc-0IcHjGhbz3o"

headers = {
    'Authorization': token
}

files = {
    'file1': ('img.jpeg', open('img.jpeg', 'rb')),
    'file2': ('img3.jpeg', open('img3.jpeg', 'rb')),
}

compare_response = requests.post('http://localhost:8000/compare/', headers=headers, files=files)

json_compare_response = json.loads(compare_response.text)

print(json_compare_response["similarity-percentage"])
