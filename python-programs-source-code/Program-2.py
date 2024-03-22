# import requests

# # Function to fetch temperature in Celsius for a given city
# def fetch_temperature(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric"
#     response = requests.get(url)
#     data = response.json()
#     if response.status_code == 200:
#         return data['main']['temp']
#     else:
#         print(f"Failed to fetch temperature data for {city}.")
#         return None

# # List of cities
# cities = ["London", "New York", "Paris", "Tokyo", "Sydney", "Beijing", "Dubai", "Mumbai", "Moscow", "Berlin"]

# celsius_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

# temperatures_celsius = list(map(fetch_temperature, cities))

# temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))

# # Displaying the temperatures in Fahrenheit for each city
# for city, temperature in zip(cities, temperatures_fahrenheit):
#     print(f"Temperature in {city}: {temperature:.2f}°F")



"""
    Use following API to get current weather
     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric"
"""
celsius_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

# List of temperatures in Celsius for 10 cities
temperatures_celsius = [22, 18, 25, 30, 16, 20, 27, 23, 19, 21]

# Using map function to apply the conversion function to each temperature
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))

# Displaying the temperatures in Fahrenheit for each city
for city, temperature in zip(range(1, 11), temperatures_fahrenheit):
    print(f"City {city}: {temperature:.2f}°F")
