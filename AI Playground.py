# Programmer: Carson Grant
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")
# Import libraries
import requests

# Define API key and base URL (replace with your own API key)
api_key = "ada71058b408099a065a3683bfb5b363"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get city name from user
city_name = input("Enter the city name: ")

# Build the URL with city name and API key
complete_url = f"{base_url}q={city_name}&appid={api_key}"

# Send request and get response
response = requests.get(complete_url)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json()

  # Extract weather information
  weather = data["main"]
  temperature = round((weather["temp"] * 9/5) - 459.67)  # Convert Kelvin to Celsius

  # Print weather information
  print(f"Weather in {city_name}:")
  print(f"Temperature: {temperature} °F")
  print(f"Description: {data['weather'][0]['description']}")
else:
  # Handle error
  print("Error: Could not retrieve weather data.")
