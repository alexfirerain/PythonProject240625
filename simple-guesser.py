num = 3
flag = True

var = ''
print('Как насчёт угадать число?')

while 7:
    var = int(input('Ваш вариант: '))
    if var == num:
        print('Угадано')
        break
    elif var > num:
        print('Нет, число поменьше ', var)
    else:
        print('Нет, число побольше', var)
