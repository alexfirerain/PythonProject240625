word = 'сударшаначакра'

if 'чакра' in word:
    print('yes')

for ch in word:
    print(ch)

# итератор range генерит последовательность от start до stop через step

for i in range(0, 3, 1): print(i)

for i in range(2, 13, 2): print(i)

# start defaults to 0, step defaults to 1
for i in range(13): print(i)

# if counter not used through the loop, it may be '_'
for _ in range(13): print('i', end='')
print()

for i in range(101):
    if i % 10 == 5:
        if i == 15:
            continue
        print(i)

for i in reversed(range(1, 101)):
    if i % 10 == 5:
        if i == 15:
            continue
        print(i)
for i in range(0, 101, 5):
    print(i, end=' ')