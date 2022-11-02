import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
BOARD_BORDER = "#"


def create_player():

    player = {'name': "Maciej",
              'weapon': "d",
              'age': 1,
              'x': PLAYER_START_X,
              "y": PLAYER_START_Y,
              "icon": PLAYER_ICON,
              "live": 100}

    krasnal = {'name': "Krasnal",
               'weapon': "Axe",
               'age': 42,
               'x': PLAYER_START_X,
               "y": PLAYER_START_Y,
               "icon": PLAYER_ICON,
               "live": 100}

    elf = {'name': "elf",
           'weapon': "sword",
           'age': 442,
           'x': PLAYER_START_X,
           "y": PLAYER_START_Y,
           "icon": PLAYER_ICON,
           "live": 200}

    # for x in player:
    #     if x == "x":
    #         break
    #     player[x] = input(f"Enter player's {x}: ")

    players = [player, krasnal, elf]
    counter = 0

    for x in players:
        counter += 1
        x = x.get('name')
        print(f'{counter}-{x}')
    x = input("Choose player by entering the number: ")
    print(players[int(x)]['name'])
    return players[int(x)]


def player_movement(board, player, key):
    if key == 's' and board[player["x"]+1][player['y']] != BOARD_BORDER:
        player["x"] += 1
    if key == 'w' and board[player["x"]-1][player['y']] != BOARD_BORDER:
        player["x"] -= 1
    if key == 'a' and board[player["x"]][player['y'] - 1] != BOARD_BORDER:
        player["y"] -= 1
    if key == 'd' and board[player["x"]][player['y'] + 1] != BOARD_BORDER:
        player["y"] += 1


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_BORDER)
    engine.put_items_on_board(board, player)
    # util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            player_movement(board, player, key)
        # util.clear_screen()


if __name__ == '__main__':
    main()
