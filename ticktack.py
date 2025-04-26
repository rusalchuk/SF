print('''ИНСТРУКЦИЯ:
1. поставьте свой символ: вводите координаты <номер строки><пробел><номер столбца>
2. нажмите <enter> и ход перейдет к сопернику
3. продолжайте, пока один из вас не победит!''')
print()

# создаем поле 3х3:
field = [['□' for i in range(3)] for j in range(3)]


def print_field(l):
    """функция для вывода поля с добавлением номеров строк и столбцов"""

    print(' ', 1, 2, 3)
    row_number = 1
    for row in l:
        print(row_number, end=' ')
        for cell in row:
            print(cell, end=' ')
        print()
        row_number += 1


def put_cross(pole=field):
    """функция постановки крестика на указанные координаты"""

    # проверка на количество координат:
    while True:
        try:
            stroka, stolbec = list(map(int, input('Задайте координаты для крестика: ').split()))
            break
        except ValueError:
            print('Координат должно быть две!')

    # проверка на корректность координат:
    while stroka not in range(1, 4) or stolbec not in range(1, 4):
        print('Введите числа от 1 до 3!')
        stroka, stolbec = list(map(int, input('Задайте координаты для крестика: ').split()))

    # проверка на свободное поле:
    while field[stroka - 1][stolbec - 1] != '□':
        print('Поле занято, попробуйте снова!')
        stroka, stolbec = list(map(int, input('Задайте координаты для крестика: ').split()))

    field[stroka - 1][stolbec - 1] = 'X'

    return pole


def put_null(pole=field):
    """функция постановки нолика на указанные координаты"""

    # проверка на количество координат:
    while True:
        try:
            stroka, stolbec = list(map(int, input('Задайте координаты для нолика: ').split()))
            break
        except ValueError:
            print('Координат должно быть две!')

    # проверка на корректность координат:
    while stroka not in range(1, 4) or stolbec not in range(1, 4):
        print('Введите числа от 1 до 3!')
        stroka, stolbec = list(map(int, input('Задайте координаты для нолика: ').split()))

    # проверка на свободное поле:
    while field[stroka - 1][stolbec - 1] != '□':
        print('Поле занято, попробуйте снова!')
        stroka, stolbec = list(map(int, input('Задайте координаты для нолика: ').split()))

    field[stroka - 1][stolbec - 1] = '○'

    return pole


def check_win(pole=field):
    """функция для проверки победы. Формирует 4 списка, отражающие 4 условия победы:
    3 одинаковых символа по горизонтали, вертикали или диагонали.
    Выводит победителя и завершает программу."""

    # победа, если 3 одинаковых символа по любой горизонтали
    wins_row = [pole[i] for i in range(3)]
    if any(all(x == 'X' for x in wins_row[i]) for i in range(3)):
        print('Крестики победили!')
        exit()
    elif any(all(x == '○' for x in wins_row[i]) for i in range(3)):
        print('Нолики победили!')
        exit()

    # победа, если 3 одинаковых символа по любой вертикали
    wins_col = [[pole[i][j] for i in range(len(pole))] for j in range(len(pole[0]))]
    if any(all(x == 'X' for x in wins_col[i]) for i in range(3)):
        print('Крестики победили!')
        exit()
    elif any(all(x == '○' for x in wins_col[i]) for i in range(3)):
        print('Нолики победили!')
        exit()

    # победа, если 3 одинаковых символа по \ диагонали
    wins_diag1 = [pole[i][i] for i in range(3)]
    if all(x == 'X' for x in wins_diag1):
        print('Крестики победили!')
        exit()
    elif all(x == '○' for x in wins_diag1):
        print('Нолики победили!')
        exit()

    # победа, если 3 одинаковых символа по / диагонали
    wins_diag2 = [pole[2][0], pole[1][1], pole[0][2]]
    if all(x == 'X' for x in wins_diag2):
        print('Крестики победили!')
        exit()
    elif all(x == '○' for x in wins_diag2):
        print('Нолики победили!')
        exit()


# запуск игрового процесса:
while True:
    print_field(field)
    put_cross(field)
    print_field(field)
    check_win(field)
    put_null(field)
    check_win(field)

