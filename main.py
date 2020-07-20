import requests
from time import sleep


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def get_chat_id(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update


def main():
    token = "1325110987:AAHkykK4bYufy1gCg-0kUwTa3Wqlq8qmDmg"
    bot = TelegramBot(token)
    update_id = bot.get_last_update()['update_id']
    while True:
        if update_id == bot.get_last_update()['update_id']:
            chat_id = bot.get_chat_id(bot.get_last_update())
            bot.send_message(chat_id, "Hello")
            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()