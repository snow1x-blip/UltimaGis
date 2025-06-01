import logging
import os

from dotenv import load_dotenv
from telebot import TeleBot
from Commands import Commands_

logging.basicConfig(level=logging.INFO)
load_dotenv()


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot = TeleBot(token)
        self.commands = Commands_(self.bot)

    def run(self):
        self.commands.register_commands()
        self.bot.polling()


def main():
    token = os.getenv('TOKEN')
    bot = TelegramBot(token)
    bot.run()


if __name__ == '__main__':
    main()
