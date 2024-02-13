import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
getResponse = requests.get(url)
print(f"Status code of GET request: {getResponse.status_code}")
print(getResponse.json())

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'userId': 1, 'title': 'New Post', 'body': 'Post content here.'}
postResponse = requests.post(url, json=data)
print(f"\nStatus code of POST request: {postResponse.status_code}")
print(postResponse.json())

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {'userId': 1, 'id': 1, 'title': 'Updated Title', 'body': 'Updated post content.'}
putResponse = requests.put(url, json=data)
print(f"\nStatus code of PUT request: {putResponse.status_code}")
print(putResponse.json())

url = 'https://jsonplaceholder.typicode.com/posts/1'
deleteResponse = requests.delete(url)
print(f"\nStatus code of DELETE request: {deleteResponse.status_code}")
print(deleteResponse.json())
