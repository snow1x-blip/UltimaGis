import logging
import lasio
import pandas as pd
from main import TelegramBot

logging.basicConfig(level=logging.INFO)


class LasToAsciiConverter:
    def convert(self, file_name):
        las = lasio.read(file_name)
        data = las.data
        df = pd.DataFrame(data)
        ascii_file_name = file_name.replace('.las', '.ascii')
        df.to_csv(ascii_file_name, sep='\t', index=False)


def main():
    token = '5806816635:AAEPihEhHMh9iXohdI9qsUjwQqUxBQlOGrU'
    bot = TelegramBot(token)
    bot.run()


if __name__ == '__main__':
    main()
