#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram import *
from telegram.ext import *
from requests import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5483568585:AAGA9LKBhtQEruB3d-ER2P06-a6KrabnLak'
WEB_URL = 'https://firangi-bot-app.herokuapp.com/'

randomPeopleText = "Random Person"
randomImageText = "Random Image"

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    #update.message.reply_text('Hi!')
    #button = KeyboardButton(
    #            text="Open the color picker!",
    #            web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"))
    #context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot Deepak!", reply_markup=ReplyKeyboardMarkup(button))
    #buttons = [[KeyboardButton(randomImageText, web_app=WebAppInfo(url="https://webtest.d1uh4zy1fq8jyc.amplifyapp.com"))], [KeyboardButton(randomPeopleText, web_app=WebAppInfo(url="https://webtest.d1uh4zy1fq8jyc.amplifyapp.com"))]]
    #context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot Deepak!", reply_markup=ReplyKeyboardMarkup(buttons))
    context.bot.send_video(chat_id=update.effective_chat.id, reply_to_message_id="Welcome to my bot Deepak!", video="https://www.youtube.com/shorts/VKGOGtuqN18")

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
 

    # Get the dispatcher to register handlers


    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    #Start the bot using webhook
    #updater.start_webhook(listen="0.0.0.0",
    #                  port=int(PORT),
    #                  url_path=TOKEN,
    #                 webhook_url = WEB_URL + TOKEN)
    #updater.bot.set_webhook(WEB_URL + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()