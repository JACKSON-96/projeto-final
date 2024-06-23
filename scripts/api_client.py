import requests

url = "http://127.0.0.1:8000/protected_route/"
headers = {
    "Authorization": "Token 99f7e666b1bd3650befe7dfd9d71e68216f8598b"
}

response = requests.get(url, headers=headers)

print(response.json())
