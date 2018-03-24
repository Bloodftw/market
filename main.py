import requests


# Апдейты
def get_update(limit, offset):
    url = "https://api.telegram.org/bot516515436:AAGfllRJOH_QRbHrgycmwq6K0p2bJsSld2Y/getUpdates"
# задаю параметры в словарь
    params = {'limit': limit, 'offset': offset}
# результат используя запрос по ЮРЛу и заданным параметрам
    result = requests.get(url, params=params)
# результат переменной переводим в Json
    encode = result.json()
    return encode['result']


# SendMessage api
def send_message(chat_id, text):
    url_send_message = "https://api.telegram.org/bot516515436:AAGfllRJOH_QRbHrgycmwq6K0p2bJsSld2Y/sendMessage"
# Нужные ключи в словарь
    parameter = {'chat_id': chat_id, 'text': text}
# Получаем запрос
    send_response = requests.post(url_send_message, params=parameter)
    return send_response
# send_message(142799662, 'text')


bot_update = get_update(5, 0)


# курс bitcoin
def get_btc():
    btc_rur_url = "https://yobit.net/api/3/ticker/btc_rur"
    btc_course = requests.get(btc_rur_url)
    encode = btc_course.json()
    return encode['btc_rur']['buy']


btc_buy = str(get_btc())


# курс etherium
def get_eth():
    eth_rur_url = "https://yobit.net/api/3/ticker/eth_rur"
    eth_course = requests.get(eth_rur_url)
    encode = eth_course.json()
    return encode['eth_rur']['buy']


eth_buy = str(get_eth())


for update in bot_update:
    chat_id = update['message']['from']['id']
    bot_answer = update['message']['text']
    last_update_id = update['update_id']
    print(update['message']['text'], update['message']['chat']['id'])

# команды управления ботом
    if bot_answer == '/start':
        send_message(chat_id, 'Онлайн курс криптовалют. Введи /btc для курса Bitcoin и /eth для курса  Etherium')
    elif bot_answer == '/btc':
        send_message(chat_id, 'Курс Bitcoin сейчас: '+btc_buy)
    elif bot_answer == '/eth':
        send_message(chat_id, 'Курс Etherium сейчас: '+eth_buy)
    get_update(1, last_update_id+1)
