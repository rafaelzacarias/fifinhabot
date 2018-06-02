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
import os
import random
import csv
import sys
from collections import defaultdict

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('COEEEEH RAPAZIAAAAAADA!')

def update(bot, update):
    update.message.reply_text('reiniciando...')
    os.system("git pull")
    update.message.reply_text('sincronizado!')
    sys.exit()

def help(bot, update):
    """Send a message when the command /help is issued."""
    commands = [
        '/duplas <nome1> <nome2>.... <nome n>',
        '/times <rating>',
        '/selecoes_masculinas <rating>',
        '/selecoes_femininas <rating>'
    ]
    update.message.reply_text("\n".join(commands))

def shuffle_pairs(bot, update):
    """Send a message when the command /duplas is issued."""
    names = update.message.text.split('/duplas ')[1].split(' ')
    random.shuffle(names)
    reply_text = "As duplas são:\n"
    for i in range(0,len(names),2):
        if (i+1)<len(names):
            reply_text += "[{}, {}] \n".format(names[i],names[i+1])
        else:
            reply_text += "\n Sobrou: [{}] ".format(names[i])
    update.message.reply_text(reply_text)

def pick_teams(bot, update):
    """Send a message when the command /times is issued."""
    rating = update.message.text.split('/times ')[1]
    reply_text = _pick_teams(teams, rating)
    update.message.reply_text(reply_text)

def pick_men_nationals(bot, update):
    """Send a message when the command /selecoes_masculinas is issued."""
    rating = update.message.text.split('/selecoes_masculinas ')[1]
    reply_text = _pick_teams(men_nationals, rating)
    update.message.reply_text(reply_text)

def pick_women_nationals(bot, update):
    """Send a message when the command /selecoes_masculinas is issued."""
    rating = update.message.text.split('/selecoes_femininas ')[1]
    reply_text = _pick_teams(women_nationals, rating)
    update.message.reply_text(reply_text)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def _pick_teams(teams, rating):
    if rating in teams:
        if len(teams[rating]) >= 2:
            reply_text = '[' + ', '.join(random.sample(teams[rating], 2)) + ']'
        else:
            reply_text = 'Nao existem times nesse rating'
    else:
        reply_text = 'Vc escolheu um rating invalido'
    return reply_text

def _load_from_file(file):
    teams = {
        '1': [],
        '1.5': [],
        '2': [],
        '2.5': [],
        '3': [],
        '3.5': [],
        '4': [],
        '4.5': [],
        '5': []
    }
    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        for (team, rating) in reader:
            teams[rating].append(team)
    return teams

teams = _load_from_file('teams.csv')
men_nationals = _load_from_file('men_nationals.csv')
women_nationals = _load_from_file('women_nationals.csv')

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.

    updater = Updater(os.getenv('TELEGRAM_TOKEN'))

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("duplas", shuffle_pairs))
    dp.add_handler(CommandHandler("times", pick_teams))
    dp.add_handler(CommandHandler("selecoes_masculinas", pick_men_nationals))
    dp.add_handler(CommandHandler("selecoes_femininas", pick_women_nationals))
    dp.add_handler(CommandHandler("update", update))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
