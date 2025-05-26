import logging
from telebot import TeleBot
from Commands import Commands_

logging.basicConfig(level=logging.INFO)


class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.bot = TeleBot(token)
        self.commands = Commands_(self.bot)

    def run(self):
        self.commands.register_commands()
        self.bot.polling()


def main():
    token = '5806816635:AAEPihEhHMh9iXohdI9qsUjwQqUxBQlOGrU'
    bot = TelegramBot(token)
    bot.run()


if __name__ == '__main__':
    main()
