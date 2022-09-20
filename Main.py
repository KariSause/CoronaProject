import COVID19Py
import telebot

token_tg_bot = ""

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot(token_tg_bot)


@bot.message_handler(commands=["start"])
def start(message):
    
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну" 
    bot.send_message(message.chat.id, send_mess, parse_mode="html")


@bot.message_handler(content_types=["text"])
def mess(message):
    final_message = ""
    get_message_bot = message.text.lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "англия":
        location = covid19.getLocationByCountryCode("ENG")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по стране: </u>\nНаселение: {location['confirmed']['country_population']}\nПоследние обновление: {date[0]}{time[0]}\nПоследние данные:\n<b>Заболевших: </b>{location['confirmed']['latest']['confirmed']:,}\n<b>Смертность: </b>{location['confirmed']['latest']['deaths']:,}"

    if final_message == "":
        date = location[0]["last_updated"].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране: </u>\nНаселение: {location[0]['country_population']}\nПоследние обновление: {date[0]}{time[0]}\nПоследние данные:\n<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертность: </b>{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)

#latest =  covid19.getLatest()
#location = covid19.getLocationByCountryCode("US")
