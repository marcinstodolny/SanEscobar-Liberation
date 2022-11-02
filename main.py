import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''

    player = {'name': "",
              'weapon': "",
              'age': 42}

    for x in player:
        player[x] = input(f"Enter player's {x}: ")

    return player

def find_player(board, PLAYER_ICON):
    for sub_list in board:
        if PLAYER_ICON in sub_list:
            return (board.index(sub_list), sub_list.index(PLAYER_ICON))


def player_movement(board, PLAYER_ICON):
    key = util.key_pressed()
    x,y = find_player(board, '@')
    if key == 's':
        board[x][y] = " "
        board[x+1][y] = PLAYER_ICON
    if key == 'w':
        board[x][y] = " "
        board[x-1][y] = PLAYER_ICON
    if key == 'a':
        board[x][y] = " "
        board[x][y-1] = PLAYER_ICON
    if key == 'd':
        board[x][y] = " "
        board[x][y+1] = PLAYER_ICON


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
