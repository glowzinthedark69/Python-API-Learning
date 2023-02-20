import requests

api_url = "https://api.restful-api.dev/objects"
response = requests.get(api_url)
print(response.json())
