#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    messages = requests.get('http://localhost:8080/').json()
    print(messages)
    update.message.reply_text('Hi Anne! I heard some things about you today. Someone said, "' +
        messages[0] + '" and someone else said, "' + messages[1] + '"... How do you feel about them? Rate from 1 to 5.')

def echo(bot, update):
    """Echo the user message."""
    if ((update.message.text == '1') | (update.message.text == '2') | (update.message.text == '3')):
        # requests.post('http://localhost:8080', data = {'response':'12'})
        update.message.reply_text('Aww don\'t feel so bad!')
    elif ((update.message.text == '4') | (update.message.text == '5')):
        # requests.post('http://localhost:8080', data = {'response':'345'})
        update.message.reply_text('That\'s great!')
    elif (update.message.text == 'Life sucks'):
        update.message.reply_text('OMG! Do you want to talk about it?')
    elif (update.message.text == 'I hate my leg'):
        update.message.reply_text('Why! I think its great!')
    else:
        update.message.reply_text('Sorry don\'t understand?')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    print("STARTING")
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("536857251:AAG5gFAdHiRKGnfvDr0mco3ozO7ngAs1dA8")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("hello", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()
print('BYE')