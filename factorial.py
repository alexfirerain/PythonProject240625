fac = 1
target = int(input('до какого числа сочтём факториал: '))

for i in range(1, target + 1):
    fac *= i
    print(fac)

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print()

"""
    запрашиваем рост
    до тех пор, пока не введено отрицательное значение
    критерий: между 140 и 180
    вывод:
        сколько прошло тест
        высочайший из прошедших
        нижайший из прошедших
        средний их прошедших
"""

min_height = 140
max_height = 180

passed = 0
max_in = float('-inf')
min_in = float('inf')

sum_in = 0
while True:
    h = float(input('Рост очередного кандидата: '))
    if h <= 0:
        break
    if min_height <= h <= max_height:
        passed += 1
        sum_in += h
        if h > max_in:
            max_in = h
        if h < min_in:
            min_in = h

avg_in = sum_in / passed
print(f'прошло {passed}, из них высочайший {max_in}, нижайший {min_in}, средний рост {avg_in:.2f}')
