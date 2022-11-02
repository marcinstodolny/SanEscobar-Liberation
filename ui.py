import os


def display_board(board):
    for item in board:
        print("".join(item))


def display_items(items_list):
    for key, value in items_list.items():
        print(f"{key} : {value}")


def display_player(player):
    os.system("")
    zzz = player

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

    for key, value in zzz.items():
        if key == "weapon":
            break
        print(f"{style.MAGENTA}{key}: {str(value)}",
              sep=' ', end=' ', flush=True)
