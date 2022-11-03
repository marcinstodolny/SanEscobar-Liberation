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


def health_level(character, character_list):
    if character["health"] <= 0:
        print("you have died!")
    if character["health"] > 0:
        print(f"You have {character['health']} health left")
    for counter, item in enumerate(character_list):
        print(f"{counter}-{item.get('name')}")
    user_choice = input("Choose player by entering the number: ")
    print(character_list[int(user_choice)]["name"])
    return character_list[int(user_choice)]


def create_board(player):
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, BOARD_BORDER)
    engine.put_items_on_board(board, player, BOARD_BORDER)
    board[BOARD_HEIGHT - 2][BOARD_WIDTH - 1] = "]"
    return board


def main():
    player = create_player()
    board = create_board(player)
    collected_items = {}
    story.intro(player['name'])
    # util.clear_screen()
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
            engine.player_movement(board, player, key, collected_items, BOARD_BORDER)
        # util.clear_screen()


if __name__ == "__main__":
    main()
