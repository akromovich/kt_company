import telebot
import states
from data_cards import *
from states import *
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup
from aiogram.utils.markdown import hlink
from telebot.custom_filters import TextFilter

state_storage = StateMemoryStorage()

bot = telebot.TeleBot('5963196823:AAGKovN54CuxoTwoxe8tHVOr9N5cDdR5ixQ', parse_mode='HTML', state_storage=state_storage)

give = ''
take = ''
amount = ''
get = ''
get2 = ''
get3 = ''
user_dict = []
karta = []

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.chat_id = None
# class Moneta:
#     def __init__(self):
#         self.Bitcoin = None
#         self.Ethereum = None
#         self.Litecoin = None
#         self.Dogecoin = None
#         self.Tether_ERC20 = None
#         self.Tether_TRC20 = None
#         self.Perfect_Money = None
#         self.Perfect_Money2 = None
#         self.AdvCash = None
#         self.AdvCash2 = None
#         self.AdvCash3 = None
#         self.QIWI = None
#         self.Payeer1 = None
#         self.Payeer2 = None
#         self.Payeer3 = None
#         self.Visa = None
#         self.UnionPay_CARD = None
#         self.UZCARD_Card = None
#         self.HUMO_Card = None
#         self.WU = None
#         self.MoneyGram = None

base = sqlite3.connect('karta.db', check_same_thread=False)
cur = base.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    # ///////////////////////
    # AKROM EDIT
    bot.send_message(message.chat.id, 'Ассалому алайкум')
    base = sqlite3.connect('karta.db')
    cur = base.cursor()
    result = cur.execute('SELECT * FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    if not bool(len(result)):
        cur.execute('INSERT INTO `karta_info`(user_id) VALUES(?)', (message.chat.id,))
    else:
        bot.send_message(message.chat.id, "сиз рўйхатдан ўтгансиз")
    base.commit()
    # AKROM EDIT
    # //////////////////////

    # user_dict[message.chat.id] = User(message)

    # db = sqlite3.connect("")
    # c = db.cursor()
    # # c.execute("""CREATE TABLE KT(
    # #             used_id char(25)
    # #             name text
    # # )""")
    #
    # c.execute("SELECT * from KT")
    # rows = c.fetchall()
    # print(rows)
    # for i in rows:
    #     if str(message.chat.id) == i[0]:
    #         bot.send_message(message.chat.id, "Siz royhatdan otgansiz")
    #         start(message)
    #
    #     else:
    #         c.execute("""INSERT INTO used_id (chat_id, name) VALUES (?, ?)""",
    #                   [message.chat.id, message.chat.first_name])
    #         db.commit()
    #         c.close()
    #         db.close()
    #         bot.send_message(message.chat.id, "Assalomu aleykum, *KT Company* telegram botiga xush kelibsiz!",
    #                          parse_mode='Markdown') "📂 Алмашувлар",
    #         start(message)

    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_menu.add("🔄 Валюта айирбошлаш","🔰 Ҳамёнлар",)
    markup_menu.add("📞 Қайта алоқа", "⚙️ Созламалар",)
    msg = bot.send_message(message.chat.id, """🤓Валюта айирбошлаш хизматига хуш келибсиз. Сиз билан кўришиб турганимиздан хурсандмиз.

☝️Эслатма: Сиз бизнинг ботимиз орқали ўз пулларингизни бошқа валюталар билан тезкор айирбошлашингиз  мумкин!""",
                           reply_markup=markup_menu)

    print(message.from_user.first_name)
    bot.register_next_step_handler(msg, get_info)


@bot.message_handler(content_types=['text'])
def get_info(message):
    if message.text == "🔄 Валюта айирбошлаш":
        Valyuta(message)
    if message.text == "📤 Бош меню":
        start(message)
    if message.text == "🔰 Ҳамёнлар":
        Xamyon(message)
    if message.text == "📞 Қайта алоқа":
        Aloqa(message)
    if message.text == "⚙️ Созламалар":
        Nastroy(message)
    if message.text == "Тилни ўзгартириш  🇷🇺 Ру/🇺🇿 Уз":
        Til(message)
    if message.text == "ℹ️ Ф.И.Ш ни ўзгартириш":
        Fio(message)
    if message.text == "Bitcoin (BTS)":
        Bitcoin(message)
    if message.text == "Ethereum (ETH)":
        Ethereum(message)
    if message.text == "Litecoin (LTC)":
        Litecoin(message)
    if message.text == "Dogecoin (DOGE)":
        Dogecoin(message)
    if message.text == "Tether ERC20 (USDT)":
        Tether_ERC20(message)
    if message.text == "Tether TRC20 (USDT)":
        Tether_TRC20(message)
    if message.text == "Perfect Money (USD)":
        Perfect_Money(message)
    if message.text == "Perfect Money (EUR)":
        Perfect_Money2(message)
    if message.text == "AdvCash (USD)":
        AdvCash(message)
    if message.text == "AdvCash (EUR)":
        AdvCash2(message)
    if message.text == "AdvCash (RUB)":
        AdvCash3(message)
    if message.text == "QIWI (RUB)":
        QIWI(message)
    if message.text == "Payeer (USD)":
        Payeer1(message)
    if message.text == "Payeer (EUR)":
        Payeer2(message)
    if message.text == "Payeer (RUB)":
        Payeer3(message)
    if message.text == "Visa (USD)":
        Visa(message)
    if message.text == "UnionPay CARD (CNY)":
        UnionPay_CARD(message)
    if message.text == "UZCARD Card (UZS)":
        UZCARD_Card(message)
    if message.text == "HUMO Card (UZS)":
        HUMO_Card(message)
    if message.text == "WU (USD)":
        WU(message)
    if message.text == "MoneyGram (USD)":
        MoneyGram(message)
    if message.text == "🚫Бекор килиш":
        print("Bekor qilindi")
        start(message)
    if message.text == "🔄 айирбошлаш":
        info(message)


@bot.message_handler(chat_types=['private'])
@bot.message_handler(content_types=['text'])
def Nastroy(message):
    if message.chat.type == 'private':
        markup_nastroy = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup_nastroy.add("Тилни ўзгартириш  🇷🇺 Ру/🇺🇿 Уз", "ℹ️ Ф.И.Ш ни ўзгартириш", "📤 Бош меню")
        bot.send_message(message.chat.id, "⚙️ Созламалар", reply_markup=markup_nastroy)


def Til(message):
    markup_til = types.InlineKeyboardMarkup(row_width=2)
    yu = types.InlineKeyboardButton(text="🇷🇺", callback_data='yu')
    uy = types.InlineKeyboardButton(text="🇺🇿", callback_data='uy')
    markup_til.add(yu, uy)
    bot.send_message(message.chat.id, """Ўзингизга маъқул бўлган тилни танланг 👇
Выберите нужный вам язык👇""", reply_markup=markup_til)


def Fio(message):
    bot.send_message(message.chat.id, """Исм ва фамилянгизни киритинг:

Мисол учун: (Иван Иванов)""")


@bot.message_handler(chat_types=['private'])
@bot.message_handler(content_types=['text'])
def Valyuta(message):
    if message.chat.type == 'private':
        markup_valyuta = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup_valyuta.add("🚫Бекор килиш")  # , "📤 Бош меню",
        markup2 = InlineKeyboardMarkup(row_width=2)
        buttons = []

        for i in range(0, len(give_list)):
            button = InlineKeyboardButton(text=give_list[i], callback_data=give_list[i])
            button2 = InlineKeyboardButton(text=Bitcoin_BTS[i], callback_data=Bitcoin_BTS[i] + '_give')
            buttons.append(button)
            buttons.append(button2)
        markup2.add(*buttons)
        bot.set_state(message.from_user.id, MyStates.phone, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['user_id'] = message.from_user.id
        bot.send_message(message.chat.id, "🔄 Валюта айирбошлаш", reply_markup=markup_valyuta)
        bot.send_message(message.chat.id, "Валюталарни танланг:\n(⬅️Бериш) ва (Олиш➡️)", reply_markup=markup2)


@bot.message_handler(chat_types=['private'])
@bot.message_handler(content_types=['zakaz'])
def info(message):
    if message.chat.type == 'private':
        markup_tel = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        tel = types.KeyboardButton("📞 Телефон ракамни юбориш", request_contact=True)
        markup_tel.add(tel)

        bot.send_message(message.chat.id, "Телефон ракамни юборинг", reply_markup=markup_tel)


@bot.callback_query_handler(func=lambda call: call.data in give_list)
def callback_query(call):
    global give
    give = call.data
    print("Giving", give)
    markup1 = InlineKeyboardMarkup(row_width=2)
    buttons = []
    a = eval(call.data)
    new_list = give_list.copy()

    for i in range(0, len(give_list)):
        if new_list[i] == call.data:
            new_list[i] = '✅️' + call.data
        button = InlineKeyboardButton(text=new_list[i], callback_data=new_list[i])
        button2 = InlineKeyboardButton(text=a[i], callback_data=take_list_call[i])
        buttons.append(button)
        buttons.append(button2)
    markup1.add(*buttons)
    bot.set_state(call.message.from_user.id, MyStates.take, call.message.chat.id)
    with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
        data['give'] = call.data

    bot.edit_message_reply_markup(call.message.chat.id,
                                  call.message.message_id,
                                  call.inline_message_id,
                                  reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: call.data in take_list_call)
def callback_query2(call):
    global take
    take = call.data
    print("Taking ", take)
    bot.set_state(call.message.from_user.id, MyStates.amount, call.message.chat.id)
    with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
        data['take'] = call.data
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "⬆️Бериш: <b>{}</b>\n"
                     "⬇️Олиш: <b>{}</b> ".format(give, take))
    msg = bot.send_message(call.message.chat.id,
                           "Бериш миқдорини <b>{}</b>да киритинг:".format(give))
    bot.register_next_step_handler(msg, Amount)


def Amount(message):
    global amount
    amount = message.text
    if message.text=='🚫Бекор килиш':
        start(message)
    else:
        msg = bot.send_message(message.chat.id, """Сиз тўлов қилмоқчи бўлган \n\n<b>{}</b> рақамни киритинг:""".format(give))
        bot.register_next_step_handler(msg, Get)


def Get(message):
    global get
    get = message.text
    if message.text=='🚫Бекор килиш':
        start(message)
    else:
        bot.send_message(message.chat.id, "Қабул қилинди.")
        msg = bot.send_message(message.chat.id, """
    Маблағ тушурмоқчи бўлган<b>{}</b> \nрақамни киритинг:""".format(take))
        bot.register_next_step_handler(msg, Get2)


def Get2(message):
    global get2
    get2 = message.text
    if message.text=='🚫Бекор килиш':
        start(message)
    else:
        msg = bot.send_message(message.chat.id, """Исм ва фамилянгизни киритинг:\n\nМисол учун: (Иван Иванов)""")
        bot.register_next_step_handler(msg, Get3)


def Get3(message):
    global get3
    get3 = message.text
    if message.text=='🚫Бекор килиш':
        start(message)
    else:
        markup_tel = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        tel = types.KeyboardButton("📞 Телефон ракамни юбориш", request_contact=True)
        back = types.KeyboardButton('🚫Бекор килиш')

        markup_tel.add(tel).add(back)
        msg = bot.send_message(message.chat.id, "Телефон ракамни юборинг", reply_markup=markup_tel)
        bot.register_next_step_handler(msg, final)


@bot.message_handler(content_types=['contact'], state=MyStates.phone)
def final(message):
    if message.chat.type == 'private':
        if message.text=='🚫Бекор килиш':
            start(message)
        else:
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['phone'] = message.contact
            bot.send_message(message.chat.id, "Қабул қилинди!")
            bot.delete_state(message.from_user.id, message.chat.id)

            msg = 'Sotish: {}\nOlish: {}\n\nMiqdori: {}\n\nSotish karta: {}\nOlish karta: {}\n\nIsmi: {}\nNomer: {}'.format(
                give,
                take,
                amount,
                get,
                get2,
                get3,
                message.contact.phone_number)
            bot.send_message(-1001899167321, "New zakaz: \n\n{}".format(msg))
            # bot.send_message(2028447300, "New zakaz: \n\n{}".format(msg)-1001899167321,)
            start(message)

@bot.message_handler()
def xamyon_delete(message):
    if message.text == "❌Хамёнларни учириш":
        print('123')
        cur.execute('UPDATE `karta_info` SET Bitcoin=?,Etherneum=?,Litecoin=?,Dogecoin=?,Tether_ERC20=?,Tether_TRC20=?,Perfect_Money=?,Perfect_Money2=?,AdvCash=?,AdvCash2=?,AdvCash3=?,QIWI=?,Payeer1=?,Payeer2=?,Payeer3=?,Visa=?,UnionPay_Card=?,UZCARD_Card=?,HUMO_Card=?,WU=?,MoneyGram=? WHERE user_id=?',('пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто','пусто',message.from_user.id))
        base.commit()
        bot.send_message(message.from_user.id,'Хамёнларингиз учирилди')

@bot.message_handler(chat_types=['private'])
@bot.message_handler(content_types=['text'])
def Xamyon(message):
    global base, cur
    bitcoin = cur.execute('SELECT `Bitcoin` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for b in bitcoin:
        pass
    ethereum = cur.execute('SELECT `Ethereum` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for e in ethereum:
        pass
    litecoin = cur.execute('SELECT `Litecoin` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for l in litecoin:
        pass
    dogecoin = cur.execute('SELECT `Dogecoin` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for d in dogecoin:
        pass
    tether_erC20 = cur.execute('SELECT `Tether_ERC20` FROM `karta_info` WHERE user_id=?',
                               (message.from_user.id,)).fetchall()
    for te in tether_erC20:
        pass
    tether_trC20 = cur.execute('SELECT `Tether_TRC20` FROM `karta_info` WHERE user_id=?',
                               (message.from_user.id,)).fetchall()
    for tt in tether_trC20:
        pass
    perfect_money = cur.execute('SELECT `Perfect_Money` FROM `karta_info` WHERE user_id=?',
                                (message.from_user.id,)).fetchall()
    for pm in perfect_money:
        pass
    perfect_money2 = cur.execute('SELECT `Perfect_Money2` FROM `karta_info` WHERE user_id=?',
                                 (message.from_user.id,)).fetchall()
    for pem in perfect_money2:
        pass
    advcash = cur.execute('SELECT `AdvCash` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for adv in advcash:
        pass
    advcash2 = cur.execute('SELECT `AdvCash2` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for advc in advcash2:
        pass
    advcash3 = cur.execute('SELECT `AdvCash3` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for advca in advcash3:
        pass
    qiwi = cur.execute('SELECT `QIWI` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for q in qiwi:
        pass
    payeer1 = cur.execute('SELECT `Payeer1` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for payeer in payeer1:
        pass
    payeer2 = cur.execute('SELECT `Payeer2` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for payeertwo in payeer2:
        pass
    payeer3 = cur.execute('SELECT `Payeer3` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for payeerthree in payeer3:
        pass
    visa = cur.execute('SELECT `Visa` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for v in visa:
        pass
    unionpay_card = cur.execute('SELECT `UnionPay_Card` FROM `karta_info` WHERE user_id=?',
                                (message.from_user.id,)).fetchall()
    for u in unionpay_card:
        pass
    uzcard_card = cur.execute('SELECT `UZCARD_Card` FROM `karta_info` WHERE user_id=?',
                              (message.from_user.id,)).fetchall()
    for uzc in uzcard_card:
        pass
    humo_card = cur.execute('SELECT `HUMO_Card` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for hu in humo_card:
        pass
    wu = cur.execute('SELECT `WU` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for w in wu:
        pass
    moneygram = cur.execute('SELECT `MoneyGram` FROM `karta_info` WHERE user_id=?', (message.from_user.id,)).fetchall()
    for mg in moneygram:
        pass

    a = 'htpps://youtube.com'
    if message.chat.type == 'private':
        markup_xamyon = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup_xamyon.add("📤 Бош меню")
        markup_xamyon.add("Bitcoin (BTS)", "Ethereum (ETH)", "Litecoin (LTC)", "Dogecoin (DOGE)", "Tether ERC20 (USDT)",
                          "Tether TRC20 (USDT)", "Perfect Money (USD)", "Perfect Money (EUR)", "AdvCash (USD)",
                          "AdvCash (EUR)", "AdvCash (RUB)", "QIWI (RUB)", "Payeer (USD)", "Payeer (EUR)",
                          "Payeer (RUB)",
                          "Visa (USD)", "UnionPay CARD (CNY)", "UZCARD Card (UZS)", "HUMO Card (UZS)", "WU (USD)",
                          "MoneyGram (USD)")
        bot.send_message(message.chat.id,
                         "🗂 Сизнинг ҳамёнларингиз:" + f"\n\nBitcoin (BTS)\n<code>{b[0]}</code>" + f"\n\nEthereum (ETH)\n<code>{e[0]}</code>" +
                         f"\n\nLitecoin (LTC)\n<code>{l[0]}</code>" + f"\n\nDogecoin (DOGE)\n<code>{d[0]}</code>" + f"\n\nTether ERC20 (USDT)\n<code>{te[0]}</code>" +
                         f"\n\nTether TRC20 (USDT)\n<code>{tt[0]}</code>" + f"\n\nPerfect Money (USD)\n<code>{pm[0]}</code>" + f"\n\nPerfect Money (EUR)\n<code>{pem[0]}</code>" +
                         f"\n\nAdvCash (USD)\n<code>{adv[0]}</code>" + f"\n\nAdvCash (EUR)\n<code>{advc[0]}</code>" + f"\n\nAdvCash (RUB)\n<code>{advca[0]}</code>" + f"\n\nQIWI (RUB)\n<code>{q[0]}</code>" +
                         f"\n\nPayeer (USD)\n<code>{payeer[0]}</code>" + f"\n\nPayeer (EUR)\n<code>{payeertwo[0]}</code>" + f"\n\nPayeer (RUB)\n<code>{payeerthree[0]}</code>" + f"\n\nVisa (USD)\n<code>{v[0]}</code>" +
                         f"\n\nUnionPay CARD (CNY)\n<code>{u[0]}</code>" + f"\n\nUZCARD Card (UZS)\n<code>{uzc[0]}</code>" + f"\n\nHUMO Card (UZS)\n<code>{hu[0]}</code>" +
                         f"\n\nWU (USD)\n<code>{w[0]}</code>" + f"\n\nMoneyGram (USD)\n<code>{mg[0]}</code>",
                         reply_markup=markup_xamyon, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def Bitcoin(message):
    global base, cur
    a = bot.send_message(message.chat.id, "Рақамни киритинг Bitcoin (BTS)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(a, Bitcoin_answer)


@bot.message_handler(content_types=['text'])
def Ethereum(message):
    b = bot.send_message(message.chat.id, "Рақамни киритинг Ethereum (ETH)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(b, Ethereum_asnwer)


@bot.message_handler(content_types=['text'])
def Litecoin(message):
    c = bot.send_message(message.chat.id, "Рақамни киритинг Litecoin (LTC)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(c, Litecoin_answer)


@bot.message_handler(content_types=['text'])
def Dogecoin(message):
    d = bot.send_message(message.chat.id, "Рақамни киритинг Dogecoin (DOGE)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(d, Dogecoin_answer)


@bot.message_handler(content_types=['text'])
def Tether_ERC20(message):
    e = bot.send_message(message.chat.id, "Рақамни киритинг Tether ERC20 (USDT)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(e, Tether_ERC20_answer)


@bot.message_handler(content_types=['text'])
def Tether_TRC20(message):
    f = bot.send_message(message.chat.id, "Рақамни киритинг Tether_TRC20 (USDT)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(f, Tether_TRC20_answer)


@bot.message_handler(content_types=['text'])
def Perfect_Money(message):
    j = bot.send_message(message.chat.id, "Рақамни киритинг Perfect Money (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(j, Perfect_Money_answer)


@bot.message_handler(content_types=['text'])
def Perfect_Money2(message):
    i = bot.send_message(message.chat.id, "Рақамни киритинг Perfect Money (EUR)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(i, Perfect_Money2_answer)


@bot.message_handler(content_types=['text'])
def AdvCash(message):
    k = bot.send_message(message.chat.id, "Рақамни киритинг AdvCash (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(k, AdvCash_answer)


@bot.message_handler(content_types=['text'])
def AdvCash2(message):
    l = bot.send_message(message.chat.id, "Рақамни киритинг AdvCash (EUR)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(l, AdvCash2_answer)


@bot.message_handler(content_types=['text'])
def AdvCash3(message):
    m = bot.send_message(message.chat.id, "Рақамни киритинг AdvCash (RUB)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(m, AdvCash3_answer)


@bot.message_handler(content_types=['text'])
def QIWI(message):
    n = bot.send_message(message.chat.id, "Рақамни киритинг QIWI (RUB)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(n, QIWI_answer)


@bot.message_handler(content_types=['text'])
def Payeer1(message):
    o = bot.send_message(message.chat.id, "Рақамни киритинг Payeer (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(o, Payeer1_answer)


@bot.message_handler(content_types=['text'])
def Payeer2(message):
    p = bot.send_message(message.chat.id, "Рақамни киритинг Payeer (EUR)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(p, Payeer2_answer)


@bot.message_handler(content_types=['text'])
def Payeer3(message):
    q = bot.send_message(message.chat.id, "Рақамни киритинг Payeer (RUB)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(q, Payeer3_answer)


@bot.message_handler(content_types=['text'])
def Visa(message):
    r = bot.send_message(message.chat.id, "Рақамни киритинг Visa (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(r, Visa_answer)


@bot.message_handler(content_types=['text'])
def UnionPay_CARD(message):
    s = bot.send_message(message.chat.id, "Рақамни киритинг UnionPay CARD (CNY)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(s, UnionPay_CARD_answer)


@bot.message_handler(content_types=['text'])
def UZCARD_Card(message):
    t = bot.send_message(message.chat.id, "Рақамни киритинг Card (UZS)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(t, UZCARD_Card_answer)
    # ///////////////////////
    # AKROM EDIT
    # bot.send_message(message.chat.id, message.chat.id)
    # base = sqlite3.connect('karta.db')
    # cur = base.cursor()
    # cur.execute('INSERT INTO `karta_info`(user_id) VALUES(?)',(message.from_user.id,))
    # base.commit()
    # AKROM EDIT
    # //////////////////////


@bot.message_handler(content_types=['text'])
def HUMO_Card(message):
    u = bot.send_message(message.chat.id, "Рақамни киритинг  HUMO Card (UZS)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(u, HUMO_Card_answer)


@bot.message_handler(content_types=['text'])
def WU(message):
    w = bot.send_message(message.chat.id, "Рақамни киритинг  WU (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(w, WU_answer)


@bot.message_handler(content_types=['text'])
def MoneyGram(message):
    x = bot.send_message(message.chat.id, "Рақамни киритинг MoneyGram (USD)\nМисол учун: (8600123456789123)")
    bot.register_next_step_handler(x, MoneyGram_answer)


@bot.message_handler(content_types=['text'])
def Bitcoin_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Bitcoin=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Ethereum_asnwer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Ethereum=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Litecoin_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Litecoin=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Dogecoin_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Dogecoin=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Tether_ERC20_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Tether_ERC20=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Tether_TRC20_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Tether_TRC20=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Perfect_Money_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Perfect_Money=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Perfect_Money2_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Perfect_Money2=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def AdvCash_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET AdvCash=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def AdvCash2_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET AdvCash2=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def AdvCash3_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET AdvCash3=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def QIWI_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET QIWI=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Payeer1_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Payeer1=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Payeer2_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Payeer2=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Payeer3_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Payeer3=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def Visa_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET Visa=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def UnionPay_CARD_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET UnionPay_Card=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def UZCARD_Card_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET UZCARD_Card=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def HUMO_Card_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET HUMO_Card=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def WU_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET WU=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


@bot.message_handler(content_types=['text'])
def MoneyGram_answer(message):
    global base, cur
    cur.execute('UPDATE `karta_info` SET MoneyGram=? WHERE user_id=?', (message.text, message.from_user.id,))
    base.commit()
    bot.send_message(message.chat.id, 'Сизнинг ҳамёнингиз сақланди.')


db = sqlite3.connect("karta.db")
c = db.cursor()

# c.execute("""CREATE TABLE karta_info (chat_id integer, name text, Bitcoin integer, Ethereum integer,
# Litecoin integer, Dogecoin integer, Tether_ERC20 integer, Tether_TRC20 integer, Perfect_Money integer,
# Perfect_Money2 integer, AdvCash integer, AdvCash2 integer, AdvCash3 integer, QIWI integer, Payeer1 integer,
# Payeer2 integer, Payeer3 integer, Visa integer, UnionPay_Card integer, UZCARD_Card integer, HUMO_Card integer,
# WU integer, MoneyGram integer)""")


# c.execute("""INSERT INTO karta_info (chat_id, name, Bitcoin, Ethereum, Litecoin, Dogecoin, Tether_ERC20, Tether_TRC20,
#                 Perfect_Money, Perfect_Money2, AdvCash, AdvCash2, AdvCash3, QIWI, Payeer1, Payeer2, Payeer3, Visa,
#                 UnionPay_Card, UZCARD_Card, HUMO_Card, WU, MoneyGram) VALUES karta_infoo)""")

c.execute("""SELECT * FROM karta_info""")
malumot = c.fetchall()
for i in malumot:
    print(i)

db.commit()
db.close()


@bot.message_handler(content_types=['text'])
def Aloqa(message):
    bot.send_message(message.chat.id, """🤖 KT Company @ktchange_bot ишончли электрон валюта айирбошлаш ботидасиз!\n
🤓Агарда сизда бизнинг хизматимиз бўйича саволларингиз ёки таклифларингиз бўлса, марҳамат, бемалол мурожаат қилинг.\n
Нима хақида ёзмокчисиз? 😉\n
@avazovsss\n
+998919823000
""")


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.polling(none_stop=True)
