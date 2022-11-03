import util
import engine
import ui
import classes
import story


PLAYER_ICON = "@"
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20
BOARD_BORDER = "#"
KING = "\u2655"


def create_own_class(character):
    for i in range(3):
        character[list(character)[i]] = input(f"Enter player's {list(character)[i]}: ")
    return character

  
def choose_precreated_class(character):
    util.clear_screen()
    ui.display_classes(character)
    user_choice = util.input_validator(
        "Choose character by entering the number: ", ["1", "2", "3"], character
    )
    util.clear_screen()
    return character[int(user_choice) - 1]


def create_player():
    human, dwarf, elf = classes.possible_classes(
        PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON
    )
    util.clear_screen()
    user_choice = util.input_validator(
        "Do you want to create your own character [1] or choose default [2]: ",
        ["1", "2"],
    )
    if int(user_choice) == 1:
        return create_own_class(human)
    if int(user_choice) == 2:
        return choose_precreated_class([human, dwarf, elf])


def create_board(player,i):
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_BORDER)
    if i < 3:
        engine.put_items_on_board(board, player, BOARD_BORDER, 5, 10)
        engine.place_enemies_on_board(board, player, BOARD_BORDER, 3, 6)
        board[BOARD_HEIGHT - 2][BOARD_WIDTH - 1] = "\u2591"
        board[BOARD_HEIGHT - 2][BOARD_WIDTH - 2] = "\u2655"
    

    return board


def main():
    player = create_player()

    boards = [create_board(player, i) for i in range(4)]
    board = boards[0]
    collected_items = {}
    story.intro(player['name'])
    util.clear_screen()
    boss_x,boss_y = 8,8
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        ui.display_player(player)
        key = util.key_pressed()
        if key == "q":
            is_running = False
        elif key == "i":
            ui.display_items(collected_items)
            input()
        elif key == "p":
            pass
        else:
            board, boards = engine.player_movement(board, player, key, collected_items, BOARD_BORDER, KING, boards)
            if len(boards) == 1:
                boss_x,boss_y = engine.boss_movement(board, boss_x, boss_y)
        util.clear_screen()


if __name__ == "__main__":
    main()
