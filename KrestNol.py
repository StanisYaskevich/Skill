a = [1, 2, 3,
     4, 5, 6,
     7, 8, 9]
b = ('', 'Перед вами поле игры "Крестики-Нолики", где каждая ячейка пронумерована.',
     '\n',
     'Первым ходит игрок, который играет за крестики, вторым, кто за нолики.',
     '\n',
     'Чтобы сходить введите номер ячейки',
     '\n',
     'Выигрывает тот, кто пермым умудрится собрать свои обозначения в ряд '
     '(вертикально, горизонтально или по диагонали).',
     '\n',
     *a[0:3], '\n', *a[3:6], '\n', *a[6:],
     '\n',
     '\n',
     'Вам понятны правила игры?')
print(*b)


def vopros():
    return 'Если все понятно, введите "y", если нет, введите "n"'


print(vopros())


def otvet(var):
    while var != 'y':
        print('Прочитайте правила еще раз! Или введите правильный вариант ответа')
        otvet(input('Y or N? '))
        break
    return var


otvet(input('Y or N? '))

print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')


def hod1(num):
    global a
    if 1 <= num <= 9:
        for j, i in enumerate(a):
            if j == (num - 1) and type(i) == int:
                a[num - 1] = 'x'
                print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
                break
            elif j == (num - 1) and type(i) == str:
                print('\n', 'Эта ячейка занята! Выберите другую.', '\n')
                print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
                hod1(int(input('Ход игрока, играющего за "Нолики". Выберите ячейку. №: ')))
            else:
                pass
    else:
        print('\n', 'Такой ячейки не существует!', '\n')
        print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
        hod1(int(input('Ход игрока, играющего за "Нолики". Выберите ячейку. №: ')))


def hod2(num1):
    global a
    if 1 <= num1 <= 9:
        for j, i in enumerate(a):
            if j == (num1 - 1) and type(i) == int:
                a[num1 - 1] = 'o'
                print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
                break
            elif j == (num1 - 1) and type(i) == str:
                print('\n', 'Эта ячейка занята! Выберите другую.', '\n')
                print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
                hod2(int(input('Ход игрока, играющего за "Нолики". Выберите ячейку. №: ')))
            else:
                pass
    else:
        print('\n', 'Такой ячейки не существует!', '\n')
        print('', *a[0:3], '\n', *a[3:6], '\n', *a[6:], '\n', sep='|')
        hod2(int(input('Ход игрока, играющего за "Нолики". Выберите ячейку. №: ')))


def proverka1():
    if (a[0] == a[1] == a[2] == 'x' or a[3] == a[4] == a[5] == 'x'
            or a[6] == a[7] == a[8] == 'x' or a[0] == a[3] == a[6] == 'x'
            or a[1] == a[4] == a[7] == 'x' or a[2] == a[5] == a[8] == 'x'
            or a[0] == a[4] == a[8] == 'x' or a[2] == a[4] == a[6] == 'x'):
        print('\n', 'Поздравляем! Выиграли "Крестики!')
    elif all([isinstance(i, str) for i in a]):
        print('Вы бились достойно, воины! Ничья!')

    else:
        hod2(int(input('Ход игрока, играющего за "Нолики". Выберите ячейку. №: ')))
        proverka2()


def proverka2():
    if (a[0] == a[1] == a[2] == 'o' or a[3] == a[4] == a[5] == 'o'
            or a[6] == a[7] == a[8] == 'o' or a[0] == a[3] == a[6] == 'o'
            or a[1] == a[4] == a[7] == 'o' or a[2] == a[5] == a[8] == 'o'
            or a[0] == a[4] == a[8] == 'o' or a[2] == a[4] == a[6] == 'o'):
        print('\n', 'Поздравляем! Выиграли "Нолики!')

    elif all([isinstance(i, str) for i in a]):
        print('Вы бились достойно, воины! Ничья!')
    else:
        hod1(int(input('Ход игрока, играющего за "Крестики". Выберите ячейку. №: ')))
        proverka1()


hod1(int(input('Ход игрока, играющего за "Крестики". Выберите ячейку. №: ')))

proverka1()
