# Коллекции (set, list, dict, tuple)
# Множества
s_empty = set()   # пустое мно
s_ready = {3, 5, 7}
s_str = {'3', '5', '7'}
s_lit = {'3', '5', '7', '5'}
s_lit.add(8)
s_lit.add('5')

print(s_empty)
print(s_ready)
print(s_str)
print(type(s_ready))
print(type(s_empty))
print(s_lit)

# Множество - набор значений одного или разных типов
# Изначально не упорядочено
# Значения уникальны, повторы игнорируются
# Но множества целых чисел почему-то сохраняют порядок

for item in s_lit:
    print(item)

print(f'число элементов в s_lit = {len(s_lit)}')
if str(3) in s_lit:
    print(True)
else:
    print(False)

print(dir(s_lit)) # Знакомство с методами класса

"""
Нет способа получить конкретный элемент множества, иначе как перебирать все, 
пока не наткнёшься на подходящий.
Есть аж три способа удалить элемент множества:
"""
s_lit.remove('5')   # вызывает исключение, если элемента нет
s_lit.discard('3')  # если не было элемента, игнорирует
print(s_lit.pop())  # удаляет и возвращает случайный элемент
# s_lit.clear()
s_lit.pop()

# if s_lit: # = множество уже не пустое, т.е. empty ~~ False
#     pass

s = set()
while (city := input('Назови город ')) != '':

    if city in s:
        print('уже было')
    else:
        s.add(city)
print(f'И так было названо {len(s)} городов')