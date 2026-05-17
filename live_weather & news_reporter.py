import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path=".env")

api_key = os.getenv("API_KEY")

print(api_key)

FILE_NAME = "weather_log.txt"

def get_weather():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("1: Search by City")
    print("2: Search by ZIP")
    choice = input("Enter Choice (1 or 2): ")

    if choice == "1":
        city = input("Enter City: ").strip()
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
        geo_res = requests.get(geo_url).json()

        if not geo_res:
            print("City Not Found")
            return
        
        lat = geo_res[0]['lat']
        lon = geo_res[0]['lon']
        
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    elif choice == "2":
        zip_code = input("Enter ZIP Code: ")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data['name']
            country = data['sys']['country']
            temp_celsius = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            print(f"{city}, {country}") 
            print(f"temperature: {temp_celsius:.2f}C.")
            print(f"Weather: {weather_desc}")
        else:
            print("Check if the city name is written correctly or through API.")

    
    
        if response.status_code == 200:
           temp_celsius = data['main']['temp']
           desc = data['weather'][0]['description']
           if temp_celsius > 30:
            advice = "It's very hot, brother, drink water!"
           elif temp_celsius < 20:
            advice = "It's cold, take off your jacket."
           else:
            advice = "The weather is fine, go for a walk."
       
           print(f"Advice: {advice}")

           with open("weather_log.txt", "a") as file:
                file.write(f" [{current_time}] | Location: {city}, {country} | Temp: {temp_celsius:.2f}C | Condition: {desc} | Note: {advice}\n")

           print("Record has been saved in file.\n")
        else:
             print("Error: Check City/ZIP or API key.\n")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("==== LIVE WEATHER MENU ====")
    print("1. Check Weather & Save Log")
    print("2. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        get_weather()
    elif choice == "2":
        print("Allah Hafiz! see you next time.")
        break
    else:
        print("Invalid Choice! Try Again.\n")
        


