print()
print('Крестики-нолики ver. 1.0')

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board(field):
    for line in field:
        for cell in line:
            print(cell, end='  ')
        print()


def check_win(field, player):
    for check in field:
        if check.count(player) == 3:
            return True

    if field[0][0] == player and field[1][0] == player and field[2][0] == player:
        return True
        # столбец 0 проверка

    if field[0][1] == player and field[1][1] == player and field[2][1] == player:
        return True
        # столбец 1 проверка

    if field[0][2] == player and field[1][2] == player and field[2][2] == player:
        return True
        # столбец 2 проверка

    if field[0][0] == player and field[0][1] == player and field[0][2] == player:
        return True
        # строка 0 проверка

    if field[1][0] == player and field[1][1] == player and field[1][2] == player:
        return True
        # строка 1 проверка

    if field[2][0] == player and field[2][1] == player and field[2][2] == player:
        return True
        # строка 2 проверка

    if field[0][0] == player and field[1][1] == player and field[2][2] == player:
        return True
        # диагональ 1 проверка

    if field[0][2] == player and field[1][1] == player and field[2][0] == player:
        return True
        # диагональ 2 проверка


current_player = 'X'

while True:
    print()
    print_board(board)
    print()
    print('Ход игрока', current_player)
    line = int(input('Введите номер строки для хода: ')) - 1
    column = int(input('Введите номер столбца для хода: ')) - 1

    if line >= 3 or column >= 3:
        print()
        print('Введите корректный номер строки / столбца (от 1 до 3)')
        continue

    if board[line][column] != '-':
        print()
        print('Эта ячейка уже занята, введите корректный номер ячейки')
        continue

    board[line][column] = current_player

    if check_win(board, current_player):
        print_board(board)
        print(f'Игрок {current_player} выиграл!')
        break

    if all([cell != '-' for line in board for cell in line]):
        print()
        print_board(board)
        print()
        print('Игра закончилась в ничью!')
        break

    current_player = 'O' if current_player == 'X' else 'X'
