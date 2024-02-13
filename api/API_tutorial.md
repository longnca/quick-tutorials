Title: API Tutorials for Complete Beginners

- Skill requirements: Basic Python knowledge

# Part 1: Introduction to APIs

## What is an API?

API is the acronym for Application Programming Interface — an intermediary that allows two applications to talk to each other. APIs are very important for creating interconnected software applications.

Analogy: API is like a *waiter* in a restaurant (`API`) taking orders (`requests`) from customers (`users`) and bringing back food (`responses`) from the kitchen (`server`). Without the waiter, the customers cannot order food and the kitchen staff cannot know any requests from the customers. Therefore, the waiters/APIs are crucial links for different people/applications to undertand and communicate with each other.

## Why Python for APIs?

Python is a great programming language for handling APIs for the following reasons:

- Simple: straightforward syntax and short learning curve are some of Python's strengths.
- Powerful libraries such as `requests`.
- Community support: Python is on the rise to become one of the most common languages in various use cases.

## Setting up environment

- Install Python
- Create a virtual env if needed.

E.g.

```bash
python3 -m venv myprojectenv
```

- Install `requests`.

## Make your first API call

Get your hands dirty, fast!

```python
import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Convert the response object to a dictionary
data = response.json()

print(f"Status code: {response.status_code}")
print(f"Complete response: {data}")
```

This code sends a GET request to the JSONPlaceholder API for a specific post and prints the response in JSON format.

The code returns the (fake) information:

```bash
Status code: 200
Complete response: {'userId': 1, 'id': 1,
 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
  'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
```

## Understanding API responses

In the code above, the status code is 200. What does it mean?

The status code indicates whether your request was successful or not, and the JSON object contains the data you requested. Common status codes include:

- `200 OK`: The request was successful.
- `404 Not Found`: The requested resource doesn't exist.
- `401 Unauthorized`: Authentication is required or has failed.
- `500 Internal Server Error`: An error occurred on the server side.

The results are in JSON format: `{key}: {value}`. We can call the keys from the dictionary that we want, for example:

```python
print(f"The User ID is: {data['userId']}")
```

Returns: `The User ID is: 1`.

## Exercises - Your turn

You will have to fetch weather data from the OpenWeatherMap API.

Step-by-Step Instructions:

- Sign up for an API key from OpenWeatherMap.
- Construct the request URL with the city name and API key. For example: Toronto ON.
- Make the request and parse the JSON response to extract and print specific weather information.

Check out my solution below.

# Part 2: Deep Dive into HTTP Methods and Handling API Responses

In this post, we will break down these concepts into simple terms, including n HTTP methods, handling API responses, and practical examples using Python's `requests` library.

## Understanding HTTP methods

### GET

A GET request is to **ask for the data** from the server. Take the exercise in previous part as example, you want to know the weather data for Toronto. You ask Open Weather Map by sending GET request, then they respond with the information in JSON format. You've completed the GET request task.

### POST

A POST request sends data to the server to **create or update** a current resource. This is like filling out a form or uploading data to a website.

### PUT

A PUT request will **replace current data with new ones**. It is like replacing a used paper towel with a new one. You do not add anything new, just replace the old or current one.

### DELETE

As the name suggests, DELETE requests are about **removing something**. It **deletes** the specified resource.

## Making API Calls with different HTTP methods

Uou can make these different types of API calls using Python's `requests` library (that's the convenient beauty of Python - simple and powerful libraries). 

Here are the syntax of API calls using `requests`:

- GET: `response = requests.get('https://api.example.com/data')`
- POST: `response = requests.post('https://api.example.com/data', data={'key': 'value'})`
- PUT: `response = requests.put('https://api.example.com/data/1', data={'key': 'value'})`
- DELETE: `response = requests.delete('https://api.example.com/data/1')`

## Handling JSON responses

**JSON** (JavaScript Object Notation) is a common format for sending and receiving data through APIs. Use `.json()` method to parse JSON response to a Python dictionary. For example:

```python
response = requests.get(url)
data = response.json() # convert JSON to a dictionary
print(data)
```

## Status codes

When making API calls, it's crucial to handle errors and understand what different HTTP **status codes** mean. 

Use the `.status_code` parameter to check the status code of server's response. Google "HTTP status codes" for more detail.

Below are some common HTTP status code.

- `200 OK`: Success!
- `401 Unauthorized`: When authentication is required and has failed or has not yet been provided..
- `404 Not Found`: The server can't find the requested resource.
- `500 Internal Server Error`: A generic error message, indicating something went wrong on the server's side.

## Exercises - Try it yourself

Let's get your hands dirty with practicing API calls for JSONPlaceholder at: <https://jsonplaceholder.typicode.com/>.

Your task is to get, post, replace, and delete (fake) data from the server of JSONPlaceholder with the guides below. Explain in your own words the results returned from the HTTP method calls.

- GET: /posts
- GET: /posts/1
- GET: /posts/1/comments
- GET: /comments?postId=1
- POST: /posts
- PUT: /posts/1
- PATCH: /posts/1
- DELETE: /posts/1

Quick question: What is the status code of the POST request? Is it 200?

Check out my sample solution below.

# Part 3: Authentication and Security with APIs

# Part 4: Advanced Features of the Requests Library

# Part 5: Building and Deploying a Simple Project Using an API

# Solutions to Exercises

## Open Weather Map API

Compare your solution with my Python code here: [Open Weather Map](openweathermap.py).

Code snippet:

```python
import requests

api_key = "your-api-key"
city = "Toronto"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
print(f"Status: {response.status_code}")

# Convert the response object to a dictionary
data = response.json()

print(f"\nTotal data: {data}")

print(f"\nWeather in {city}: {data['weather'][0]['description']}.")
```

## HTTP method calls with JSONPlaceholder API

Check my Python code here: [HTTP methods](http_methods.py).

Code snippet:

```python
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
```