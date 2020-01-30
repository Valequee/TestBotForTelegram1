import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start', 'tostart'])
def welcome(message):
    sti = open('stickers/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Рандомный стикер")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("6")
    item7 = types.KeyboardButton("7")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Welcome, <b>{0.first_name}</b>!\nI`m - <b>{1.first_name}</b>, bot, which was created by Valeque ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['HackMode'])
def HackMode(message):
    sti = open('stickers/AnimatedStickerForBot.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Go to HELL!!")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("/tostart")
    item7 = types.KeyboardButton("7")
 
    markup.add(item4, item5, item6)
    bot.send_message(message.chat.id, "Well, <b>{0.first_name}</b>!\nNow you huesos ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['list'])
def listing(message):
    bot.send_message(message.chat.id, 'List of available commands:\n1. /start\n2. /reply\n3. /list')
 
@bot.message_handler(content_types=['text', 'sticker'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Bigger than zero", callback_data='bigger')
            item2 = types.InlineKeyboardButton("Smaller than zero", callback_data='smaller')
 
            markup.add(item1, item2)

            bot.send_message(message.chat.id,'..........', reply_markup=markup)
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text == 'Go to HELL!!':
            bot.send_message(message.chat.id, 'HellScream')
        elif message.text == 'Рандомный стикер':
            bot.send_sticker(message.chat.id, random.choice(config.STICKERS))            
        else :
            bot.send_message(message.chat.id, 'Ignoring u...')

 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'bigger':
                bot.send_message(call.message.chat.id, 'Your number is:')
                bot.send_message(call.message.chat.id, str(random.randint(0, 100)))
            elif call.data == 'smaller':
                bot.send_message(call.message.chat.id, 'Your number is:')
                bot.send_message(call.message.chat.id, str(random.randint(-100, 0)))
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=False)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="test")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
