import requests, json

api_key = '7abbf1993ddde2bc4ee77e2cd4f8099b'

def get_ip_address():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
    except Exception as e:
        print("Error getting IP address:", e)
    return None

def get_location_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        print("Error getting location info:", e)
    return None

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

ip_address = get_ip_address()
if ip_address:
    location_info = get_location_info(ip_address)
    if location_info:
        latitude, longitude = location_info['loc'].split(',')
        weather_data = get_weather_info(latitude, longitude, api_key)
        display_weather_info(weather_data)