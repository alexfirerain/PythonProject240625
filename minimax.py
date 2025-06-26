total = 0
mult = 1
N = 5
max_n = -float('inf')
min_n = float('inf')
for _ in range(N):
    num = int(input('вводим целое число '))
    total += num
    mult *= num
    if num > max_n:
        max_n = num
    if num < min_n:
        min_n = num

average = total / N

print('-------')
print(f'Сумма: {total}')
print(f'Произведение: {mult}')
print(f'Среднее: {average}')
print(f'Максимум: {max_n}')
print(f'Минимум: {min_n}')

