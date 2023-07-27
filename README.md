# AutoLocateWeather

## Overview
AutoLocateWeather is a simple Python project that fetches and displays the current weather information of a person's location using their IP address. The app utilizes the "ipinfo.io" API to obtain the user's IP address and location details, and then uses the OpenWeatherMap API to fetch real-time weather data based on the user's latitude and longitude.

## Features
- Automatic retrieval of the user's IP address.
- Display of the user's location details, such as city, region, and country.
- Real-time weather information, including temperature (in Celsius), and weather description.

## Requirements
- Python 3.x
- `requests` library. Install it using the following command:

    ```pip install requests```
- An API key from OpenWeatherMap. Sign up on the OpenWeatherMap website to get an API key.

## How to Use
1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed along with the `requests` library.
3. Sign up on the OpenWeatherMap website to get an API key.
4. Open the `weather_app.py` file and replace `'YOUR_OPENWEATHERMAP_API_KEY'` with your actual API key.
5. Open a terminal or command prompt in the project directory.
6. Run the weather app using the following command:


## How it Works
The Weather App uses two APIs to provide weather information. First, it retrieves the user's IP address using the "ipinfo.io" API. Then, it fetches location details (latitude, longitude, city, etc.) based on the IP address. Using this location information, it makes a request to the OpenWeatherMap API to get the current weather data. The weather data is displayed in the terminal for the user's location.

## Note
- The weather information is provided in Celsius units.
- This app is for personal use and educational purposes only. Do not use it for any commercial or production purposes.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgments
- The Weather App uses the "ipinfo.io" API to fetch the user's IP address and location information.
- It also utilizes the OpenWeatherMap API to obtain real-time weather data.

## Contact
For any questions or feedback, please feel free to contact the project maintainer:
- Name: Pranish Kedia
- Email: pranishk12@gmail.com
