import story
import sys
import os
from operator import itemgetter
import colorama


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
    class style:
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE = "\033[37m"
        UNDERLINE = "\033[4m"
        RESET = "\033[0m"

    names = ["name", "health"]
    for key, value in player.items():
        if key in names:
            print(
                f"{style.MAGENTA}{key}: {str(value)}{style.RESET}",
                sep=" ",
                end=" ",
                flush=True,
            )
    print("                   Press H for help")


def show_statistic(player, all_stats):
    print(f"Damage: {player['dmg']}\nArmor: {player['armor']}")
    for k, v in all_stats.items():
        print(f"{k}: {v}")


def help():
    print(
        f"Possible keys:\nWASD: moving character\nI: show inventory\nQ: quit game\nP: show statistic\nO: items meaning"
    )


def icon_meaning(icons, enemy):
    for k, v in icons.items():
        print(f"{k}  {v}")
    print(f"{enemy[0]}   Enemy")

def health_level(player, enemy, current_player):
    if current_player != player and player["health"] <= 0:
        print(story.game_over)
        sys.exit()
    elif enemy["health"] <= 0:
        print(f"{enemy['name']} has been defeated")


def show_dmg(player, player2, dmg, block):
    if dmg - block <= 0:
        print(f"{player['name']} missed")
    else:
        print(f"{player['name']} dealt {dmg - block} dmg to {player2['name']}")


def hall_of_fame(collected_items):
    new_result = []
    for x, y in collected_items.items():
        new_result.extend((x, str(y)))
    try:
        with open("hall_of_fame.csv", "r") as file:
            lines = file.readlines()
        top_5 = [element.replace("\n", "").split(";") for element in lines]
    except IOError:
        return []
    top_5.append(new_result)
    top = sorted(top_5, key=lambda x: int(x[1]), reverse=True)
    with open("hall_of_fame.csv", "w") as file:
        for i, record in enumerate(top):
            if i == 5:
                break
            row = ";".join(record)
            file.write(row + "\n")
    for i, s in enumerate(top[:5], 1):
        print(i, "-", *s)
