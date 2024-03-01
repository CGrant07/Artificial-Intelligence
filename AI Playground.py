# Programmer: Carson Grant
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")
import requests
import json

def get_weather(api_key, zip_code):
  """
  Retrieves weather information for a US zip code using the OpenWeatherMap API.

  Args:
      api_key: Your OpenWeatherMap API key.
      zip_code: The US zip code to get weather for.

  Returns:
      A dictionary containing weather information, or None if an error occurs.
  """

  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
  # You can get a free API key at https://openweathermap.org/
  url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid=YOUR_API_KEY"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving weather data: {e}")
    return None

  data = json.loads(response.content)
  return data

# Example usage
api_key = "ada71058b408099a065a3683bfb5b363"  # Replace with your actual API key
zip_code = "your_zip_code"

weather_info = get_weather(api_key, zip_code)

if weather_info:
  # Print some of the retrieved weather information
  print(f"Weather in {zip_code}:")
  print(f"  Temperature: {weather_info['main']['temp']} Kelvin")
  print(f"  Description: {weather_info['weather'][0]['description']}")
else:
  print("Unable to retrieve weather information for", zip_code)