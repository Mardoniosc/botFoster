# coding=utf-8
import os
from telebot import TeleBot

from mensagens.mensagens import get_frase_random, get_cumprimento_message

bot = TeleBot(os.environ['BOT_TOKEN_FOSTER'])

@bot.message_handler(commands=['start', 'help'])
def send_start_message(message):
  bot.reply_to(message, 'Olá '+ message.from_user.first_name
                        +", eu sou o Foster "
                        "\nAbaixo a lista de comandos que eu respondo"
                        "\nDigite algum para eu lhe ajudar!"
                        "\n\n/olá, /oi, /oii, /eae para um comprimento amigavel"
                        "\n\n/frase para mostrar uma frase"
                        "\n\n/start ou /help para mostrar os comandos novamente"
                        "\n\n /info para informações sobre bot e seu desenvolvedor"
                        )


# opções escolhida do menu acima
@bot.message_handler(commands=['frase'])
def send_frase(message):
  frase = get_frase_random()
  bot.reply_to(message, frase)

@bot.message_handler(commands=['info', 'donio'])
def send_people(message):
  bot.reply_to(message, 'Olá meu nome é Foster\n'
                        'Fui criado por Mardonio S Costa com BotFather'
                        '\nUltima atualização: 09/07/2020'
                        '\nCodigo fonte disponivel no github: https://github.com/Mardoniosc/bottelegram'
                        '\nPara mais informações pode entrar em contato com @Mardoniosc no telegram'
                        )

@bot.message_handler(commands=['oi', 'olá', 'oii', 'eae'])
def send_cumprimento(message):
    bot.reply_to(message, get_cumprimento_message(message))
