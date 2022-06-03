import requests
import googletrans
import json
from googletrans import Translator
translator = Translator()

api_key = "0f7f2e1617e82c0568cd3747ece3c8be"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Введите название города : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

pog = response.json()

if pog["cod"] != "404":

    per = pog["main"]

    temperature = per["temp"]

    pressure = per["pressure"]

    humidity = per["humidity"]

    otv = pog["weather"]

    weather_description = otv[0]["description"]

    ar = translator.translate((

          "\n Тemperature = " +
                    str((round(temperature-273))) + "°C" +
          "\n Atmospheric pressure  = " +
                    str((round((pressure/133.3)*100))) + "mm.rt.st." +
          "\n Humidity ( as a percentage ) = " +
                    str(humidity) + " % " +
          "\n Weather = " + str(weather_description)), dest='ru')

    print(ar.text)

else:

    print("Город не найден, повторите попытку")