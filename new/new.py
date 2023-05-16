# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# from data_cards import *
# from states import *
#
# bot = telebot.TeleBot("5901967904:AAFfYl2l8IdipXzW1g0m34mowHjDt5H1aZU", parse_mode='HTML', state_storage=state_storage)
#
# give = ''
# take = ''
#
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     # bot.set_state(message.from_user.id, MyStates.give, message.chat.id)
#     # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#     #     data['user_id'] = message.from_user.id
#     markup2 = InlineKeyboardMarkup(row_width=2)
#     buttons = []
#
#     for i in range(0, len(give_list)):
#         button = InlineKeyboardButton(text=give_list[i], callback_data=give_list[i])
#         button2 = InlineKeyboardButton(text=Bitcoin_BTS[i], callback_data=Bitcoin_BTS[i] + '_give')
#         buttons.append(button)
#         buttons.append(button2)
#     markup2.add(*buttons)
#     bot.send_message(message.chat.id, "Rasm yuboring", reply_markup=markup2)
#
#
# @bot.callback_query_handler(func=lambda call: call.data in give_list)  # state=MyStates.give
# def callback_query(call):
#     global give
#     give = call.data
#     markup1 = InlineKeyboardMarkup(row_width=2)
#     buttons = []
#     a = eval(call.data)
#     new_list = give_list.copy()
#
#     for i in range(0, len(give_list)):
#         if new_list[i] == call.data:
#             new_list[i] = '✅️' + call.data
#         button = InlineKeyboardButton(text=new_list[i], callback_data=new_list[i])
#         button2 = InlineKeyboardButton(text=a[i], callback_data=take_list_call[i])
#         print(a[i] + ' ' + button2.callback_data)
#         buttons.append(button)
#         buttons.append(button2)
#     markup1.add(*buttons)
#
#     bot.edit_message_reply_markup(call.message.chat.id,
#                                   call.message.message_id,
#                                   call.inline_message_id,
#                                   reply_markup=markup1)
#
#     # bot.set_state(call.message.from_user.id, MyStates.take, call.message.chat.id)
#     # with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
#     #     data['give'] = call.data
#     #
#     # print(data['give'])
#
#
# @bot.callback_query_handler(func=lambda call: call.data in take_list_call)  # , state=MyStates.take
# def callback_query2(call):
#     global take
#
#     take = call.data
#     print("HUMO TAKE ISHLADI")
#     bot.delete_message(call.message.chat.id, call.message.message_id)
#     # with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
#     #     data['take'] = call.data
#     # bot.send_message(call.message.chat.id,
#     #                  "Siz <b>{}</b> ni <b>{}</b> ga o'tkazmoqchisiz".format(data['give'], data['take']))
#     # bot.delete_state(call.message.from_user.id, call.message.chat.id)
#     bot.send_message(call.message.chat.id,
#                      "Siz <b>{}</b> ni <b>{}</b> ga o'tkazmoqchisiz".format(give, take))
#
#
# # bot.add_custom_filter(custom_filters.StateFilter(bot))
# bot.polling(none_stop=True)


# 23442123, 'avazovsss', 123123123,
#                 234234234, 345345345, 456456456, 567567567, 678678678, 789789789, 890890890, 098098098, 987987987,
#                 876876876, 765765765, 654654654, 543543543, 432432432, 321321321, 190190190, 290290290, 390390390,
#                 490490490, 590590590

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_cards import *
from states import *
from telebot import types
from telebot import custom_filters

bot = telebot.TeleBot("5901967904:AAFfYl2l8IdipXzW1g0m34mowHjDt5H1aZU", parse_mode='HTML', state_storage=state_storage)


@bot.message_handler(content_types=['text'])
def start(message):
    bot.set_state(message.from_user.id, MyStates.give, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['user_id'] = message.from_user.id
    markup2 = InlineKeyboardMarkup(row_width=2)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup1.add("🚫Бекор килиш", "🔄 айирбошлаш")  # , "📤 Бош меню",
    buttons = []

    for i in range(0, len(give_list)):
        button = InlineKeyboardButton(text=give_list[i], callback_data=give_list[i])
        button2 = InlineKeyboardButton(text=Bitcoin_BTS[i], callback_data=Bitcoin_BTS[i] + '_give')
        buttons.append(button)
        buttons.append(button2)
    markup2.add(*buttons)
    bot.send_message(message.chat.id, "🔄 Валюта айирбошлаш", reply_markup=markup1)
    bot.send_message(message.chat.id, """Валюталарни танланг: (⬅️Бериш) ва (Олиш➡️)""",
                     reply_markup=markup2)


@bot.message_handler(content_types=['text'])
def get_info(message):
    if message.text == "🚫Бекор килиш":
        start(message)
    if message.text == "🔄 айирбошлаш":
        phone(message)


@bot.message_handler(content_types=['contact'])
def phone(message):
    markup_tel = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    phonee = types.KeyboardButton("📞 Телефон ракамни юбориш", request_contact=True)
    markup_tel.add(phonee)

    bot.send_message(message.chat.id, "Телефон ракамни юборинг", reply_markup=markup_tel)


# @bot.message_handler(content_types=['zakaz']):
# markup_tel = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
# tel = types.KeyboardButton("📞 Телефон ракамни юбориш", request_contact=True)
# markup_tel.add(tel)
#
# bot.send_message(message.chat.id, "Телефон ракамни юборинг", reply_markup=markup_tel)

@bot.callback_query_handler(func=lambda call: call.data in give_list, state=MyStates.give)  #: call.data in give_list
def callback_query(call):
    # print("Birinchi handler call.data: ", call.data)
    a = eval(call.data)

    new_list = give_list.copy()
    markup1 = InlineKeyboardMarkup(row_width=2)
    buttons = []

    for i in range(0, len(give_list)):
        if new_list[i] == call.data:
            new_list[i] = '☑️' + call.data
        button = InlineKeyboardButton(text=new_list[i], callback_data=new_list[i])
        button2 = InlineKeyboardButton(text=a[i], callback_data=a[i] + '_take')
        # print(button2)
        buttons.append(button)
        buttons.append(button2)
    markup1.add(*buttons)

    bot.edit_message_reply_markup(call.message.chat.id,
                                  call.message.message_id,
                                  call.inline_message_id,
                                  reply_markup=markup1)

    bot.set_state(call.message.from_user.id, MyStates.take, call.message.chat.id)
    with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
        data['give'] = call.data

    print('Berish: ', data['give'])


@bot.callback_query_handler(func=lambda call: call.data in take_list_call)  #: , state=MyStates.take
def callback_query2(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
        data['take'] = call.data
    print('Olish: ', data['take'])
    bot.send_message(call.message.chat.id,
                     "Siz <b>{}</b> ni <b>{}</b> ga o'tkazmoqchimisiz".format(data['give'], data['take']))
    bot.delete_state(call.message.from_user.id, call.message.chat.id)

    address = str(data['give']) + " " + " " + str(data['take'])

    bot.send_message(-754849019, 'New zakaz \n{}'.format(address))

    # bot.send_message(-1001899167321, 'New zakaz {}'.format(address))


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.polling(none_stop=True)
