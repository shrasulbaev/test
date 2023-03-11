import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types



new_list = []
news_url_list = []
news_image_list =[]


#Парсер всего что в ТЗ 
def parse():
    url = 'https://kaktus.media/?lable=8&date=2023-03-10&order=time'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    news1 = soup.find('div', 
    class_ = 'Tag--articles').find_all('div', 
    class_ = 'Tag--article')
    # print(news1)
    global new_list, news_url_list, news_image_list
    sum_ = 0
    for news_ in news1:
        head = news_.find('a', class_ = 'ArticleItem--name').text
        news_url = news_.find('a', 
        class_ = 'ArticleItem--name').get('href')
        news_url_list.append(news_url)
        news_img = news_.find('img', 
        class_ = 'ArticleItem--image-img').get('src')
        news_image_list.append(news_img)
        sum_ = sum_ + 1
        new_list.append(f'{sum_}. {head}')
    print(news_image_list)

    # print(news_url_list)
parse()

def news_text_parser(i):
    
    url = news_url_list[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    news1 = soup.find('div', class_ = 'BbCode').text
    print(news1)





token = '6172229824:AAFShAj0VGv8NuT9Ux6qZhSDarlCeaNuxOg'

bot = telebot.TeleBot(token)



keyboard = telebot.types.InlineKeyboardButton(True)
button1 = telebot.types.KeyboardButton('quit')


@bot.message_handler(commands = ['start'])
#Кнопка Quit
 #создаем команду


def news_list(message):
    bot.send_message(message.chat.id, '\n'.join(new_list[0:20]))
    

    bot.send_message(message.chat.id, 'Введите номер новости!')
@bot.message_handler(content_types = 'text')
def news_choose(message):
    if message.text.lower() in '1':
        bot.send_message(message.chat.id, '\n'.join(new_list[0:1]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[0:1]))
    elif message.text.lower() in '2':
        bot.send_message(message.chat.id, '\n'.join(new_list[1:2]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[1:2]))

    elif message.text.lower() in '3':
        bot.send_message(message.chat.id, '\n'.join(new_list[2:3]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[2:3]))
    elif message.text.lower() in '4':
        bot.send_message(message.chat.id, '\n'.join(new_list[3:4]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[3:4]))
    elif message.text.lower() in '5':
        bot.send_message(message.chat.id, '\n'.join(new_list[4:5]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[4:5]))
    elif message.text.lower() in '6':
        bot.send_message(message.chat.id, '\n'.join(new_list[5:6]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[5:6]))
    elif message.text.lower() in '7':
        bot.send_message(message.chat.id, '\n'.join(new_list[6:7]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[6:7]))
    elif message.text.lower() in '8':
        bot.send_message(message.chat.id, '\n'.join(new_list[7:8]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[7:8]))
    elif message.text.lower() in '9':
        bot.send_message(message.chat.id, '\n'.join(new_list[8:9]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[8:9]))
    elif message.text.lower() in '10':
        bot.send_message(message.chat.id, '\n'.join(new_list[9:10]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[9:10]))
    elif message.text.lower() in '11':
        bot.send_message(message.chat.id, '\n'.join(new_list[10:11]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[10:11]))
    elif message.text.lower() in '12':
        bot.send_message(message.chat.id, '\n'.join(new_list[11:12]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[11:12]))
    elif message.text.lower() in '13':
        bot.send_message(message.chat.id, '\n'.join(new_list[12:13]))    
        bot.send_message(message.chat.id, '\n'.join(news_url_list[12:13]))
    elif message.text.lower() in '14':
        bot.send_message(message.chat.id, '\n'.join(new_list[13:14]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[13:14]))
    elif message.text.lower() in '15':
        bot.send_message(message.chat.id, '\n'.join(new_list[14:15]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[14:15]))
    elif message.text.lower() in '16':
        bot.send_message(message.chat.id, '\n'.join(new_list[15:16]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[15:16]))
    elif message.text.lower() in '17':
        bot.send_message(message.chat.id, '\n'.join(new_list[16:17]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[16:17]))
    elif message.text.lower() in '18':
        bot.send_message(message.chat.id, '\n'.join(new_list[17:18]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[17:18]))
    elif message.text.lower() in '19':
        bot.send_message(message.chat.id, '\n'.join(new_list[18:19]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[18:19]))
    elif message.text.lower() in '20':
        bot.send_message(message.chat.id, '\n'.join(new_list[19:20]))
        bot.send_message(message.chat.id, '\n'.join(news_url_list[19:20]))
    else:
        bot.send_message(message.chat.id, 'введите номер новости')


# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
#     markup.add(button1)
#     bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)



bot.polling(non_stop = True)    