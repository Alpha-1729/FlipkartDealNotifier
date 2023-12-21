import os
import telebot


class TelegramClient:
    def __init__(self):
        self.telegram_bot_key = os.environ.get("TELEGRAM_BOT_KEY")
        self.telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

        if self.telegram_bot_key is None or self.telegram_chat_id is None:
            raise Exception("Please configure TELEGRAM_BOT_KEY and TELEGRAM_CHAT_ID in environment variables.")

        self.bot = telebot.TeleBot(self.telegram_bot_key)

    def sent_message(self, message):
        self.bot.send_message(self.telegram_chat_id, message)
