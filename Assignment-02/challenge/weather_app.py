import responses
import info

API_KEY = "a657a4978215d33bbdc774f9721995e3"

city = input("Enter city name: ")

response = responses.getweather(API_KEY, city)

if response.get("cod") != 200:
    print("Error:", response.get("message", "City not found or API error!"))
    exit()

temp = info.gettemp(response)
humidity = info.gethumidity(response)
wind = info.getwind(response)
timezone = info.gettimezone(response)

print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind} m/s")
print(f"Timezone: {timezone}")
