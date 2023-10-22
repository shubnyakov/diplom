import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку'),
    ('low', 'Вывод самых дешевых отелей в городе'),
    ('high', 'Вывод самых дорогих отелей в городе'),
    ('best_deal', 'Вывод отелей, наиболее подходящих по заданным параметрам'),
    ('history', 'Вывод истории поиска отелей')

)
