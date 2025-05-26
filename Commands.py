import os
from LAS_block import LasToAsciiConverter


class Commands_:
    def __init__(self, bot):
        self.bot = bot

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.bot.send_message(
                message.chat.id,
                'Привет! Я могу конвертировать '
                'LAS-файлы в формат ASCII. Отправьте мне LAS-файл.'
            )

    def handle_file(self):
        @self.bot.message_handler(content_types=['document'])
        def handle_file(message):
            file_id = message.document.file_id
            file_name = message.document.file_name

            if file_name.endswith('.las'):
                self.bot.send_message(
                    message.chat.id,
                    'Файл получен. Конвертирую...'
                )
                file = self.bot.get_file(file_id)
                downloaded_file = self.bot.download_file(file.file_path)

                with open(file_name, 'wb') as f:
                    f.write(downloaded_file)

                converter = LasToAsciiConverter()
                converter.convert(file_name)
                ascii_file_name = file_name.replace('.las', '.ascii')

                with open(ascii_file_name, 'rb') as f:
                    self.bot.send_document(message.chat.id, f)

                os.remove(file_name)
                os.remove(ascii_file_name)
                self.bot.send_message(
                    message.chat.id,
                    'Конвертированный файл отправлен.'
                )

            else:
                self.bot.send_message(
                    message.chat.id,
                    'Неправильный формат файла. Отправьте LAS-файл.'
                )

    def register_commands(self):
        self.start()
        self.handle_file()
