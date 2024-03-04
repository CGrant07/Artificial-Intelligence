# Programmer: Carson Grant
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")
import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = 'ada71058b408099a065a3683bfb5b363'

def get_weather(zip_code):
  """
  Gets weather data for a given zip code using the OpenWeatherMap API.

  Args:
      zip_code (str): The zip code to get weather data for.

  Returns:
      dict: A dictionary containing the weather data, or None if an error occurs.
  """

  # Base URL for the OpenWeatherMap API
  url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={API_KEY}"

  # Make the API request
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    return data
  else:
    print(f"Error: {response.status_code}")
    return None

# Get the zip code from the user
zip_code = input("Enter a US zip code: ")

# Get the weather data
weather_data = get_weather(zip_code)

# Check if data was retrieved successfully
if weather_data:
  # Print the weather data
  print(f"Weather in {weather_data['name']}:")
  print(f"\t- Description: {weather_data['weather'][0]['description']}")
  print(f"\t- Temperature: {(weather_data['main']['temp'] - 273.15):.2f} degrees Celsius")
else:
  print("Error: Unable to retrieve weather data.")