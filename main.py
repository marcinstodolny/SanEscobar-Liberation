import util
import engine
import ui
import classes
import story
import colorama

PLAYER_ICON = f"{colorama.Fore.CYAN}@{colorama.Fore.RESET}"
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_START_X = 1
PLAYER_START_Y = BOARD_WIDTH - 2

BOARD_BORDER = "#"
KING = colorama.Fore.YELLOW + "\u2655" + colorama.Fore.RESET
WIZARD = colorama.Fore.YELLOW + "\u26E4" + colorama.Fore.RESET


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


def create_board(player, i):
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_BORDER, i)
    if i < 3:
        engine.put_items_on_board(board, player, BOARD_BORDER, 10, 13)
        engine.place_enemies_on_board(board, player, BOARD_BORDER, 5, 6)
        board[BOARD_HEIGHT - 2][BOARD_WIDTH - 1] = "\u2591"
        if i > 0:
            board[1][0] = "\u2588"
        board[BOARD_HEIGHT - 2][BOARD_WIDTH - 2] = KING
        if i == 1:
            board[18][1] = WIZARD
    return board


def main():
    util.clear_screen()
    story.title()
    player = create_player()
    boards = [create_board(player, i) for i in range(4)]
    board = boards[0]
    collected_items = {}
    current_board = 0
    all_stats = {"items": 0}
    util.clear_screen()
    # story.intro(player['name'])
    util.clear_screen()
    boss_x, boss_y = 8, 8
    game(
        player, collected_items, boards, board, current_board, boss_x, boss_y, all_stats
    )


def game(
    player, collected_items, boards, board, current_board, boss_x, boss_y, all_stats
):
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        ui.display_player(player)
        key = util.key_pressed()
        if key in ["q", "o", "p", "h", "i"]:
            is_running = key_options(
                key, collected_items, player, is_running, all_stats
            )
        else:
            board, current_board = engine.player_movement(
                board,
                player,
                key,
                collected_items,
                BOARD_BORDER,
                KING,
                boards,
                current_board,
                all_stats,
            )
            if current_board == 3:
                boss_x, boss_y = engine.boss_movement(board, boss_x, boss_y)
        util.clear_screen()


def key_options(key, collected_items, player, is_running, all_stats):
    if key == "q":
        is_running = False
    elif key == "i":
        ui.display_items(collected_items)
        input("click enter to continue ")
    elif key == "o":
        ui.icon_meaning(engine.ITEMS_MEANING, engine.ENEMIES)
        input("click enter to continue ")
    elif key == "p":
        ui.show_statistic(player, all_stats)
        input("click enter to continue ")
    elif key == "h":
        ui.help()
        code = input("click enter to continue ")
        if code == "escobar":
            player["health"] = 1000
            player["dmg"] = 100
    return is_running


if __name__ == "__main__":
    main()
