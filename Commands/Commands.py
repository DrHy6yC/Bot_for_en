from aiogram.types import BotCommand

start_command = BotCommand(command='start', description='Кнопка для внесения пользователя в БД')
stop_bot_command = BotCommand(command='stop', description='Кнопка для остановки бота')
get_private_command = BotCommand(command='get_keyboard', description='Кнопка для получения индивидуальной клавиатуры')
help_command = BotCommand(command='help', description='Помощь по боту')

my_command = [start_command, stop_bot_command, get_private_command
              ]