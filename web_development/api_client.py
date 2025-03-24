import requests
response = requests.get("https://api.github.com/users/octocat")
print("User Info:", response.json())