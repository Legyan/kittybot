import os

from dotenv import load_dotenv
from telegram import Bot
import requests

load_dotenv()
auth_token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = Bot(token=auth_token)

URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()

text = 'Вам телеграмма!'
bot.send_message(chat_id, text)
bot.send_photo(chat_id, response[0].get('url'))
