import story
import sys
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
        
def health_level(player, enemy,current_player):
    if current_player != player:
        if player["health"] <= 0:
            print(story.game_over)
            sys.exit()
        print(f"You have {player['health']} health left")
    elif enemy['health'] > 0:
        print(f"Enemy has {enemy['health']} health left")
    else:
        print(f"{enemy['name']} has been defeated")
            
def show_dmg(player, player2, dmg, block):
    if dmg - block <= 0:
        print(f"{player['name']} have missed")
    else:
        print(f"{player['name']} dealt {dmg - block} dmg to {player2['name']}")