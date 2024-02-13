# Open Weather Map API

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