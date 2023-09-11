# Крестики-нолики

# Задача
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими.
# Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё усмотрение.
# Главное, чтобы в игру можно было поиграть через терминал с вашего компьютера.

import random


class empty_table():

    def get_empty_table():
        empty_table = [['x/y   1    2    3'],
                       ['  1 ', ' _ |', ' _ |', ' _ '],
                       ['  2 ', ' _ |', ' _ |', ' _ '],
                       ['  3 ', ' _ |', ' _ |', ' _ ']]
        for i in range(0, len(empty_table)):
            for j in range(0, len(empty_table[i])):
                print(empty_table[i][j], end=' ')
            print()
        return empty_table


def check_coordinates():
    x, y = int(input("x = ")), int(input("y = "))
    while not 1 <= x <= 3 or not 1 <= y <= 3:
        print('Wrong number, try again')
        x, y = int(input()), int(input())
    return int(x), int(y)


def game():
    player_number = random.randint(1, 2)
    x_list, y_list = [], []
    count = 1
    game_table = empty_table.get_empty_table()
    while count <= 9:
        print(f'Player {player_number} enters coordinates (x, y): ', end='')
        x, y = check_coordinates()
        x_list.append(x)
        y_list.append(y)
        move = (x, y)

        if count >= 2:
            for i in range(len(coord_list)):
                while coord_list[i] == move:
                    print('Coordinates are already used, enter again')
                    x, y = check_coordinates()
                    move = (x, y)
        for i in range(0, len(game_table)):
            for j in range(0, len(game_table[i])):
                if i == x and j == y:
                    if player_number == 1:
                        game_table[i][j] = ' X  '
                    else:
                        game_table[i][j] = ' O  '
                print(game_table[i][j], end=' ')
            print()
        coord_list = list(zip(x_list, y_list))
        count += 1
        player_number = 3-player_number

    game_table = game_table[1:4]
    del game_table[0][0]
    del game_table[1][0]
    del game_table[2][0]
    return game_table


game_table = [[' _ |', ' _ |', ' _ '],
              [' _ |', ' _ |', ' _ '],
              [' _ |', ' _ |', ' _ ']]


def victory_check(game_table):
    result = 'Dead heat!'
    count = 0
    for i in range(len(game_table)):
        if game_table[i][0] == game_table[i][1] == game_table[i][2]:
            if game_table[i][0] == ' X  ':
                result = 'Player 1 WINS!!!'
            else:
                result = 'Player 2 WINS!!!'
            count += 1
    for j in range(len(game_table)):
        if game_table[0][j] == game_table[1][j] == game_table[2][j]:
            if game_table[0][j] == ' X  ':
                result = 'Player 1 WINS!!!'
            else:
                result = 'Player 2 WINS!!!'
            count += 1
    if game_table[0][0] == game_table[1][1] == game_table[2][2] or game_table[2][0] == game_table[1][1] == game_table[0][2]:
        if game_table[0][0] == ' X  ':
            result = 'Player 1 WINS!!!'
        else:
            result = 'Player 2 WINS!!!'
    if count > 1:
        result = 'Dead heat!'

    return result


def main():
    print('Start the game:')
    print()

    table_game = game()
    print(victory_check(table_game))


if __name__ == "__main__":
    main()
