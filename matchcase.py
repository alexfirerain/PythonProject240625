print('Возможны ходы:\n\tL - налево\n\tR - направо\n\tF - вперёд')

# since Py3.10
while True:
    ch = input('Вводим ')
    match ch:
        case 'L' | 'l':
            print('пошли налево')
        case 'R' | 'r':
            print('пошли налево')
        case 'F' | 'f':
            print('пошли налево')
        case 'Q' | 'q':
            print('вышли')
            break
        case _:
            print('стоим')
