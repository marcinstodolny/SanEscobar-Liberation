
import os
from operator import itemgetter


def display_board(board):
    for item in board:
        print(" ".join(item))


def display_items(items_list):
    for key, value in items_list.items():
        print(f"{key} : {value}")


def display_classes(players):
    for counter, classes in enumerate(players, start=1):
        print(f"{counter} - {classes['name']}")


def display_player(player):
    class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    for key, value in player.items():
        if key == "weapon":
            break
        print(f"{style.MAGENTA}{key}: {str(value)}{style.RESET}",
              sep=' ', end=' ', flush=True)


def hall_of_fame():
    player_score = ['Anna', 9]
    print(player_score)
    try:
        with open("hell_of_fame.csv", "r") as file:
            lines = file.readlines()
        file = [element.replace("\n", "").split(";") for element in lines]
        print(len(file))
        for s in file:

            print(*s)
    except IOError:
        return []

    top = sorted(file, key=lambda x: int(x[1]), reverse=True)

    top5 = []
    for x, i in enumerate(top):
        if x == 5:
            break
        top5.append(i)

    with open("hell_of_fame.csv", "w") as file:
        for record in top5:
            row = ";".join(record)
            file.write(row + "\n")
