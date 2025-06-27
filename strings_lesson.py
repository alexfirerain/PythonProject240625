"""
строка Питона является коллекцией (стало быть, итерируемой).
единичный символ и строка не различаются в Питоне.
символ это тоже строка, стало быть.
при этом строка неизменна, при изменении создаётся новая.

"""
s = ''
print(dir(s))
print(id(s))
s += 'привет'
print(s)
print(id(s))
s += ', чувак'
print(s)
print(id(s))

print(s[0])
# s[3] = 'И' # строка неизменна по натуре
print(s[-1])  # но можно от конца, через минус

a = 'язык Питон'
# vowels = {'и', 'е', 'а', 'о', 'у', 'ы',
#           'я', 'ю', 'э', 'ё'}
vowels = 'иеаоуыяюэё'
counter = 0
for vowel in a:
    if vowel in vowels:
        counter += 1
print(f'гласных в "{a}" всего {counter}')

for index in range(len(s)):
    print(s[index])

# задача: исправить букву в строке
sob = 'сабака'
codes = ''
# for i in range(len(sob)):
#     if i == 1:
#         res += 'о'
#     else:
#         res +=sob[i]

for i in range(len(sob)):
    codes += 'о' if i == 1 else sob[i]

print(codes)

# таблица символов
# і°µ
u = '\u2603'
print(u)
print('уникод снеговика: ', ord('☃'))

# две удобные функции:
# ord(ch) = десятеричный код символа в Уникоде
# chr(ch) = символ по Уникоду

print(chr(9731))
print(chr(176))
g = '\u0176'
print(g)
print(chr(17650))

# строка -> набор кодов

word = input()
codes = set()
for letter in word:
    codes.add(ord(letter))
print(codes)

word_back = ''
for code in codes:
    word_back += chr(code)
print(word_back)

# # Д/З Цезарь: e - зашифровать, d - расшифровать, q - выйти {меню}
# rus_abc = 'абвгдеёжзийклмнопрстуфхцшщъыьэюя'
# caesar = input('дай зашифрую: ')
# res = ''
# for letter in caesar:
#     for key in rus_abc:
#
#     index_in =



# методы строк
# ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
Д / З взять строку, каждую букву умножить столькожды, какова ея позиция
"""
phrase = 'язык Python'
print(phrase.lower())
print(phrase.upper())
print(phrase.capitalize())
print(phrase.title())
print(phrase * 3)
print('Телевизор'.count('е'))
print('fuck'.index('u'))
print(word.strip()) # удаляет символы (пробел по умолчанию) с начала и конца
print(word.lstrip()) # удаляет символы (пробел по умолчанию) с начала
print(word.rstrip()) # удаляет символы (пробел по умолчанию) с конца
print("ротор".strip("р"))
temp = input('Введите ввод: ').strip()

word = input('размажем: ')
res = ''
for i in range(len(word)):
    res += word[i] * (i + 1)
print(res)