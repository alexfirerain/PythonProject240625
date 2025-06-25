# while True:
#     user_answer = input('Который час?\n')
#
#     if user_answer == "пока" or user_answer == "bye":
#         break
#
#     hour = int(user_answer)
#
#     if hour > 23: hour = 23
#     if hour < 0: hour = 0
#
#     if 7 <= hour <= 11:
#         greeting = "Доброго утречка!"
#     elif 11 < hour <= 18:
#         greeting = "Доброго дня!"
#     elif 18 < hour <= 22:
#         greeting = "Доброго вечера!"
#     else:
#         greeting = "Доброй ночи!"
#
#     print(greeting)
# print('Пока)')

while True:
    word = input('Введите слово, не короче четырёх букв: ')
    if not word : print('а иди-ка ты')
    if word == 'stop' or word == 'хватит': break
    if len(word) < 4:
        print('не годится')
    else:
        print('спасибо, слово "' + word + '" имеет длину', len(word))

word1 = 'veni'
word2 = 'vidi'
word3 = 'vici'

print(word1, word2, word3)