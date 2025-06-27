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

##############
coins = [5, 4, 5]

# def fake_check(coin_set):
#     if coin_set[0] == coin_set[1]:
#         return 3
#     if coin_set[0] > coin_set[1]:
#         return 2
#     return 1

def fake_check(coin_set):
    return 3 if coin_set[0] == coin_set[1]\
        else 2 if coin_set[0] > coin_set[1]\
        else 1


# def fake_check(coin_a, coin_b, coin_c):
#     if coin_a == coin_b:
#         return coin_c
#     if coin_a > coin_b:
#         return coin_c
#     return coin_a

# print(fake_check(3, 2, 3))


print('Из этих монет фейковой является монета №' + str(fake_check(coins)))




