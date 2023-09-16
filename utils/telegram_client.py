import os
import requests
import urllib.parse


class TelegramClient:
    def __init__(self):
        self.telegram_bot_key = os.environ.get("TELEGRAM_BOT_KEY")
        self.telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

        if self.telegram_bot_key is None or self.telegram_chat_id is None:
            raise Exception("Please configure TELEGRAM_BOT_KEY and TELEGRAM_CHAT_ID in environment variables.")

        self.telegram_post_url = r"https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=".format(
            self.telegram_bot_key, self.telegram_chat_id)

    def sent_message(self, message):
        url = "{}{}".format(self.telegram_post_url, urllib.parse.quote_plus(message))
        requests.post(url)
