import requests
api_key  = "94c3f5791d9a920e838db3a33a885abd"
city_name = input("enter city name : ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
print(url)
req = requests.get(url)
weather_data = req.json()

if weather_data["cod"]!= "404":
    main = weather_data["main"]
    current_temperature = round(main["temp"]-273.15,2)
    current_humidity =main["humidity"]
    weather =weather_data["weather"]
    weather_description = weather[0]["description"]
    print("Temperature (in celsius unit) = " + f'{current_temperature}'+
    "\n humidity (in percentage) = " + f'{current_humidity}' + 
    "\n description = "+ f'{weather_description}')
else:
    print("city hot found")