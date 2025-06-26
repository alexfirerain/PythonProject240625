"""
ax + bx +c = 0
a, b, c (c !=0)
[ D = b^2 - 4a*c ]
if D < 0
    no roots
if D = 0
    one root
    x = -b / 2a
if D > 0
    two roots
    x1 = (-b + D^(1 / 2)) / 2a
    x2 = (-b - D^(1 / 2)) / 2a
"""

print('решение квадратного уравнения\n')
a = float(input('введите коэффициент \'a\': '))
b = float(input('введите коэффициент \'b\': '))
c = float(input('введите коэффициент \'c\': '))
print(f'уравнение имеет вид "{a}x^2 + {b}x + {c}", верно?')
if input() == 'да':
    D = b ** 2 - 4 * a * c
    if D < 0:
        print('извините, корней нет')
    if D == 0:
        x = -b / 2 * a
        print('x =', x)
    if D > 0:
        x1 = (-b + D ** (1 / 2)) / 2 * a
        x2 = (-b - D ** (1 / 2)) / 2 * a
        print('x1 =', x1, '\nx2 =', x2)
else:
    print('тогда попытайте судьбу в следующий раз')
