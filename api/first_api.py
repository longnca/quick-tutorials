import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Convert the response object to a dictionary
data = response.json()

print(f"Status code: {response.status_code}")
print(f"Complete response: {data}")
print(f"The User ID is: {data['userId']}")