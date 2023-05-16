# colors = ['Orange', 'Red', 'Blue', 'Green']
# colors.insert(0, 'Violet')
# colors.insert(2, 'Purple')
#
# print(colors)
#
# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# del colors[-1]
# colors.remove('Green')
#
# print(colors)
#
# l = [int(i) for i in input().split()]
# x = l.index(min(l))
# y = l.index(max(l))
# l[x], l[y] = max(l), min(l)
# print(*l)
#
# chars = [c for c in 'abcdefgd']
# print(chars)
#
# cubes = [i ** 3 for i in range(10, 21)]
# print(cubes)
#
# squares = [i ** 2 for i in range(10)]
# print(squares)
#
# zeros = [0 for i in range(10)]
# print(zeros)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [s[1:] for s in keywords]
#
# print(new_keywords)
#
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [s for s in keywords if len(s) >= 5]
#
# print(new_keywords)
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# print([len(i) for i in keywords])
#
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#             'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [s[1:] for s in keywords]
#
# print(new_keywords)
#
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)
# print(*[int(i) ** 3 for i in input().split()])
#
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61,
# -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97,
# 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26,
# 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] < a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
#             flag = False
#     if flag:
#         break
# print(a)
#
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90,
# 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
# -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
# -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
# b = []
# while len(a) > 0:
#     b.append(min(a))
#     a.remove(min(a))
# a = b
# print(a)


# def Amount(message):
#     global amount
#     amount = message.text
#
#     bot.send_message(message.chat.id, """Сиз тўлов қилмоқчи бўлган
#
# <b>{}</b> рақамни киритинг:""".format(give))
#
#
# def Get(message):
#     global get
#     get = message.text
#
#     markup_tel = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     tel = types.KeyboardButton("📞 Телефон ракамни юбориш", request_contact=True)
#     markup_tel.add(tel)
#     msg = bot.send_message(message.chat.id, "Телефон ракамни юборинг", reply_markup=markup_tel)
#     bot.register_next_step_handler(msg, final)
