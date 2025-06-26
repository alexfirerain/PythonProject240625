# print('отсчёт')
# counter = 0 # обнуленье счётчика
# while counter < 5:
#     print(f'итерация №{counter + 1}')
#     counter += 1
# print('counter =', counter)
#
# print('обратный отсчёт')
# while counter > 0:
#     counter -= 1
#     print(f'итерация №{counter + 1}')
# print('counter =', counter)

def quint_iterator(basement, increment):
    counter = 0
    ceiling = 5
    while counter < ceiling:
        counter += 1
        basement += increment
        print(f'число {basement}')



quint_iterator(0, 1)
quint_iterator(6, -1)

