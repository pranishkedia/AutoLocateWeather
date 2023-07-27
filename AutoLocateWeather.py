import requests

api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

# Function to get the user's IP address using ipinfo.io API
def get_ip_address():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
    except Exception as e:
        print("Error getting IP address:", e)
    return None

# Function to get location details using ipinfo.io API with the provided IP address
def get_location_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        if response.status_code == 200: # status codee 200 means successful
            data = response.json()
            return data
    except Exception as e:
        print("Error getting location info:", e)
    return None

# Function to get weather data using OpenWeatherMap API with provided latitude, longitude, and API key
def get_weather_info(latitude, longitude, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        print("Error getting weather info:", e)
    return None

# Function to display weather information
def display_weather_info(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celcius = temperature_kelvin - 273.15
        description = weather_data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature_celcius:.0f} °C")
        print(f"Description: {description}")
    else:
        print("Weather information not available.")

# Main part of the code
ip_address = get_ip_address()
if ip_address:
    location_info = get_location_info(ip_address)
    if location_info:
        latitude, longitude = location_info['loc'].split(',')
        weather_data = get_weather_info(latitude, longitude, api_key)
        display_weather_info(weather_data)
