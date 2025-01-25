import requests
import matplotlib.pyplot as plt

API_KEY = '2438902f55697b6d5829248d8e65aa92'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
def get_weather_data(city_name):

    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {city_name}. Please check the city name.")
        return None

def display_weather_chart(weather_data, city_name):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    uv_index = 0.4 

    print(f"Weather Data for {city_name}:")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Condition: {weather_data['weather'][0]['description'].capitalize()}")
    print(f"UV Index: {uv_index}")

    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (km/h)', 'UV Index']
    values = [temperature, humidity, wind_speed, uv_index]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])
    plt.ylim(0, 70)
    plt.ylabel('Values')
    plt.title(f'Weather Data for {city_name}')
    plt.show()

def main():
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)
    if weather_data:
        display_weather_chart(weather_data, city_name)

if __name__ == "__main__":
    main()