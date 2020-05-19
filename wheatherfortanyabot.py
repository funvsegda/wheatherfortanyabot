# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim

import pyowm
import telebot
geolocator = Nominatim(user_agent="my-application")
owm = pyowm.OWM('474aa6c3eaa25de108d60c26b90ebaab', language = "ua")
bot = telebot.TeleBot("1250822859:AAH7Ak2fSYWrkXY7tVmBvGff84_Wr-UntS4")


#print((location.latitude, location.longitude))

#print(location.address)


@bot.message_handler(content_types=['text'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    try:
        if message.text == "Лох" or message.text == "ЛОХ":

            print(str(message.chat.id) + " ищет " + message.text)
            bot.reply_to(message, "Сам лох")

        else:

                print(str(message.chat.id) + " ищет " + message.text)
                try:
                    location = geolocator.geocode(message.text)
                except AttributeError:
                    answer = "Не знайшов такого...: " + "\n"

                except UnboundLocalError:
                    answer = "Не знайшов такого...: " + "\n"

                else:

                    observation = owm.weather_at_coords( location.latitude, location.longitude )
                    w = observation.get_weather()
                    temp = w.get_temperature('celsius')["temp"]
                    wind = w.get_wind()["speed"]
                    humidity = w.get_humidity()
                    status = w.get_detailed_status()
                    answer = "В локації " + '(' + location.address + ')' + " зараз " + status + ": " + "\n"
                    answer += "\n\n" + "Температура повітря: " + str(temp) + "\n\n"
                    answer += "Швидкість вітру: " + str(wind) + " м/с" + "\n\n"
                    answer += "Вологість: " + str(humidity) + " %" + "\n\n"
                    print(status, str(temp), str(wind), str(humidity))

                    if float(temp) < 10:
                        answer += "Зараз холодно, одягайтеся тепліше!"
                    elif float(temp) < 20:
                        answer += "Можна одягнутися легко!"
                    else:
                        answer += "Ну і жара!"

                    bot.send_message(message.chat.id, answer)
    except AttributeError:
        answer = "Не знайшов такого...: "

    except UnboundLocalError:
        answer = "Не знайшов такого...: "
bot.polling(none_stop = True)

