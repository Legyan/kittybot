import logging
import os

import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='main.log'
)

URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    """Запрос изображения у CatAPI."""
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    """Оправка изображения получателю."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    logging.info(f'Запрос котика от {name}')
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    """Обработчик поступившей команды /start."""
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['хочу котика']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )

    context.bot.send_photo(chat.id, get_new_image())


def say_hi(update, context):
    """Обработчик поступившего текстового сообщения."""
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Привет, я KittyBot!')


def main():
    """Осно"""
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('хочу котика'),
                                                  new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
