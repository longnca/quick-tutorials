# Import library
import requests

# GET request
getResponse = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print(f"Status code of GET request: {getResponse.status_code}")
print(f"Complete response: {getResponse.json()}")
a
# Check the keys in the JSON dictionary
print("Keys in the JSON dictionary: ")
for key in getResponse.json().keys():
    print(key)

# POST request
postResponse = requests.post('https://jsonplaceholder.typicode.com/posts', 
                         {'userId':1, 'title':'testing-title-1', 'body':'testing-body-1'})

# Check if the request is successful
print(f"Status code of POST request: {postResponse.status_code}")
# View the server's response content
print(f"The data that we just posted to the server: {postResponse.json()}")

# PUT request
putResponse = requests.put('https://jsonplaceholder.typicode.com/posts/1',{'userId':1, 'title':'new-title', 'body': 'new-body'})

# Check if the request is successful
print(f"Status code of PUT request: {putResponse.status_code}")
# View the server's response content
print(f"The data that we just replaced on the server: {putResponse.json()}")

# DELETE request
deleteResponse = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request is successful
print(f"Status code of DELETE request: {deleteResponse.status_code}")
# View the server's response content (if any)
print(deleteResponse.json())