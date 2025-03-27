import requests
response = requests.get(url="https://api.github.com/users/Munir-Alam")
print(response.json())
# go