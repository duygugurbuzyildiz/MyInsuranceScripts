import requests
from pprint import pprint

# Test Authentication 
url = "http://localhost:5000/api/v1/token"

response = requests.post(
        url,
        json={"email":"jd@myinsuranceapp.com", "password":"passwordjd"}
    )

print(f"{url}: {response.status_code}")
token = response.json()["token"]

# Test Users Endpoint
url = "http://localhost:5000/api/v1/users"

response = requests.get(url, headers={"authorization": "Bearer " + token})

print(f"{url}: {response.status_code}")
pprint(response.json())

# TestProducts Endpoint
url = "http://localhost:5000/api/v1/products"

response = requests.get(url, headers={"authorization": "Bearer " + token})
print(response.status_code)
pprint(response.json())

# Test Web Page
url= "http://localhost:5000/"

response4 = requests.get(url)

if response.status_code != 200:
    print(f"Error: {url}")
print(response.status_code)
print(response.text)

