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
    return encode('result')

# SendMessage api
def send_message(chat_id, text):
    url_send_message = "https://api.telegram.org/bot516515436:AAGfllRJOH_QRbHrgycmwq6K0p2bJsSld2Y/sendMessage"
# Нужные ключи в словарь
    params = {'chat': chat_id, 'text': text}
# Получаем запрос
    requests.get(url_send_message, params=params)

# Cryptocurrencies exchange
def get_currency_value(target):
    crypto_url = "https://api.cryptonator.com/api/ticker/" + target + "rur"
    request_result = requests.get(crypto_url)
    encode = request_result.json()
    return encode(request_result)

# Передаем курс в переменную
    bitcoin_to_rur = get_currency_value('btc')
    ethereum_to_rur = get_currency_value('eth')

# Получаем апдейты
bot_update = get_update(5, 0)
# отвечаем на апдейты
# вывод нужного ключа из словаря
updates = [
    {"id": 100, "message": "test 0"},
    {"id": 101, "message": "test 1"},
    {"id": 102, "message": "test 2"},
    {"id": 103, "message": "test 3"},
]

for update in updates:
    update_message = update["id"]
    print(update_message)
