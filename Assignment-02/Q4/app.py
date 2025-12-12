import requests

api_key = "03170114e220a2bb333f872154995204"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q=pune&appid=03170114e220a2bb333f872154995204"
response = requests.get(url)
if response.status_code == 200:
    weather = response.json()
    temp_celsius = weather['main']['temp'] - 273.15
    print("Temperature (°C):", round(temp_celsius, 2))
    print("Humidity:", weather['main']['humidity'])
    print("Wind Speed:", weather['wind']['speed'])
else:
    print("City not found or API error!")
