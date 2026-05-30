import requests

def weather_info(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        current = data['current_condition'][0]
        print(f"City : {city}")
        print(f"Temperature : {current['temp_C']}°C")
        print(f"Feel like :{current['FeelsLikeC']}°C")
        print(f"Humidity : {current['humidity']}%")
        print(f"Weather : {current['weatherDesc'][0]['value']}")
        print(f"Wind Speed : {current['windspeedKmph']} km/h")

    except Exception as e:
        print(f"Error fetching weather information: {e}")

while True:
    city = input("Enter the name of the city (or 'quit' to exit): ")
    if city.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    weather_info(city)