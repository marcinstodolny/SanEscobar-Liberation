import random
import enemies
import story
import ui
import util
from time import sleep
import colorama

ITEMS_MEANING = {
    "\U000026CF": "Pick",
    "\U0000269A": "Wand",
    "\u26E8": "Shield",
    "\u2E38": "Dagger",
    "\u2764": "Potion",
}
DMG_ITEMS = {"Dagger": 2, "Wand": 3, "Pick": 1}
ARMOR_ITEMS = {"Shield": 1}
HEALTH_ITEMS = {"Potion": 50}
ENEMIES = [colorama.Fore.RED + "\u2620" + colorama.Fore.RESET]
WIZARD = [colorama.Fore.YELLOW + "\u26E4" + colorama.Fore.RESET]


def create_board(width, height, BOARD_BORDER, i):
    board = [
        [
            BOARD_BORDER if check_border(height, j) or check_border(width, i) else " "
            for i in range(width)
        ]
        for j in range(height)
    ]
    if i == 0:
        wall_row(board, width)
    elif i == 1:
        second_map(board, height, width)
    elif i == 2:
        wall_column(board, height)
    return board


def wall_row(board, width, start=0):

    for i in range(start, len(board) - 3, 3):
        if i % 2 == 0:
            for j in range(
                width - 3,
            ):
                board[i][j] = "#"
        else:
            for j in range(3, width):
                board[i][j] = "#"


def wall_column(board, height, start=0):
    for i in range(start, len(board[0]) - 3, 4):
        if i % 8 == 4:
            for j in range(height - 3):
                board[j][i] = "#"
        else:
            for j in range(3, height):
                board[j][i] = "#"


def second_map(board, height, width):
    wall_row(board, int(width / 2 - 2), 4)
    wall_column(board, int(height), int(height - 8))


def check_border(direction, iterator):
    return iterator in [0] + [direction - k for k in [0, 1]]


def put_player_on_board(board, player):
    for sub_list in board:
        if player["icon"] in sub_list:
            board[board.index(sub_list)][sub_list.index(player["icon"])] = " "
    board[player["x"]][player["y"]] = player["icon"]


def put_items_on_board(board, player, BOARD_BORDER, min_num, max_num):
    item_number = random.randint(min_num, max_num)

    items_icon = list(ITEMS_MEANING.keys())
    for _ in range(item_number):
        x, y = random.randint(1, len(board) - 1), random.randint(1, len(board[0]) - 1)
        if board[x][y] not in [player["icon"], BOARD_BORDER] + items_icon:
            board[x][y] = random.choice(items_icon)
        else:
            item_number += 1


def place_enemies_on_board(board, player, BOARD_BORDER, min_num, max_num):
    enemies_number = random.randint(min_num, max_num)
    for _ in range(enemies_number):
        x, y = random.randint(1, len(board) - 1), random.randint(1, len(board[0]) - 1)
        if (
            board[x][y]
            not in [player["icon"], BOARD_BORDER] + list(ITEMS_MEANING.keys()) + ENEMIES
        ):
            board[x][y] = random.choice(ENEMIES)
        else:
            enemies_number += 1


def king(king_icon, key, board, player, collected_items):
    if board[player["x"]][player["y"]] == king_icon:
        if count_enemies(board) > 0:
            story.king_speach_1()
            if key == "s":
                player["x"] -= 1
            elif key == "d":
                player["y"] -= 1
        else:
            story.king_speach_2()
            collected_items["Key"] = 1
        input("Press enter to continue ")
        util.clear_screen()


def count_enemies(board):
    return sum(row.count(ENEMIES[0]) for row in board)


def player_movement(
    board,
    player,
    key,
    collected_items,
    border,
    king_icon,
    boards,
    current_board,
    all_stats,
):
    keys = {"s": ["x", 1], "w": ["x", -1], "a": ["y", -1], "d": ["y", 1]}
    x, y = 0, 0
    if key in ["s", "w", "a", "d"]:
        if keys[key][0] == "x":
            x = keys[key][1]
        elif keys[key][0] == "y":
            y = keys[key][1]
    move(key, board, player, collected_items, king_icon, border, x, y)
    board, current_board = check_for_collision(
        board, player, collected_items, boards, current_board, all_stats
    )
    return board, current_board


def check_for_collision(
    board, player, collected_items, boards, current_board, all_stats
):
    item_enemy_check(board, player, collected_items, all_stats)
    if board[player["x"]][player["y"]] in ["\u2588", "\u2591"]:
        board, current_board = change_board(player, boards, current_board)
    if current_board == 3:
        boss_battle_check(board, player, collected_items, all_stats)
    return board, current_board


def move(key, board, player, collected_items, king_icon, border, x=0, y=0):
    if board[player["x"] + x][player["y"] + y] != border:
        player["x"] += x
        player["y"] += y
        if key in ["s", "d"]:
            king(king_icon, key, board, player, collected_items)


def change_board(player, boards, current_board):
    doors = boards[current_board][player["x"]][player["y"]]
    if doors == "\u2588":
        current_board -= 1
        player["x"] = len(boards[current_board]) - 2
        player["y"] = len(boards[current_board][0]) - 2
    elif doors == "\u2591":
        current_board += 1
        player["x"] = 1
        player["y"] = 1
    board = boards[current_board]
    return board, current_board


def boss_battle_check(board, player, collected_items, all_stats):
    location = board[player["x"]][player["y"]]
    if location not in [" ", "#"]:
        util.clear_screen()
        fight_with_enemy(player, all_stats, enemies.boss(player["name"]))
        ui.hall_of_fame(collected_items)
        story.outro(player, all_stats)


def item_enemy_check(board, player, collected_items, all_stats):
    location = board[player["x"]][player["y"]]
    if location in list(ITEMS_MEANING.keys()):
        item = ITEMS_MEANING[location]
        if item not in HEALTH_ITEMS:
            if item in collected_items:
                collected_items[item] += 1
            else:
                collected_items[item] = 1
            statistics("items", all_stats)
        equipment_to_stats(item, player)
    elif location in ENEMIES:
        fight_with_enemy(player, all_stats)
    elif location in WIZARD:
        story.story_wizard(player["name"])
        player["health"] += 100


def equipment_to_stats(item, player):
    if item in list(DMG_ITEMS.keys()):
        player["dmg"] += DMG_ITEMS[item]
    elif item in list(ARMOR_ITEMS.keys()):
        player["armor"] += ARMOR_ITEMS[item]
    elif item in list(HEALTH_ITEMS.keys()):
        player["health"] += HEALTH_ITEMS[item]


def fight_with_enemy(player, all_stats, boss=False):
    if boss:
        enemy = boss
        fight = [player, boss]
    else:
        enemy = random.choice(enemies.possible_classes())
        fight = [player, enemy]
    current_round = 0
    util.clear_screen()
    enemies_picture = story.enemies_list()
    battle(enemy, enemies_picture, fight, player, current_round, all_stats)


def battle(enemy, enemies_picture, fight, player, current_round, all_stats):
    while enemy["health"] > 0:
        print(enemies_picture[enemy["name"]])
        print(
            f"You have {player['health']} hp                    {enemy['name']} has {enemy['health']} hp"
        )
        current_player = fight[current_round % 2]
        current_enemy = fight[(current_round + 1) % 2]
        damage = random_damage(current_player)
        attack(damage, current_enemy, current_player, enemy, player)
        sleep(1)
        current_round += 1
        util.clear_screen()
    statistics("Won battles", all_stats)


def attack(damage, current_enemy, current_player, enemy, player):
    if damage - current_enemy["armor"] > 0:
        current_enemy["health"] -= damage - current_enemy["armor"]
        ui.show_dmg(current_player, current_enemy, damage, current_enemy["armor"])
        sleep(0.25)
        ui.health_level(player, enemy, current_player)
    else:
        ui.show_dmg(current_player, current_enemy, damage, current_enemy["armor"])
    return current_enemy


def random_damage(player):
    return random.randint(int(player["dmg"] * 0.5), int(player["dmg"] * 1.5))


def statistics(stat, all_stats):

    if stat in all_stats:
        all_stats[stat] += 1
    else:
        all_stats[stat] = 1


def boss_coordinates(boss_x, boss_y):
    boss_x += random.randint(-1, 1)
    boss_y += random.randint(-1, 1)
    if boss_x > 12:
        boss_x = 11
    elif boss_x < 3:
        boss_x = 4
    if boss_y > 20:
        boss_y = 19
    elif boss_y < 3:
        boss_y = 4
    return boss_x, boss_y


def boss_movement(board, boss_x_input, boss_y_input):
    boss_x, boss_y = boss_x_input, boss_y_input
    row = 0
    for i in enumerate(story.small_boss):
        if i[1] == "\n":
            row += 1
            continue
        elif row > 0:
            board[boss_x + row][boss_y + int(i[0]) - 10 * row] = " "
        elif row == 0:
            board[boss_x + row][boss_y + int(i[0])] = " "
    boss_x, boss_y = boss_coordinates(boss_x_input, boss_y_input)
    row = 0
    for i in enumerate(story.small_boss):
        if i[1] == "\n":
            row += 1
            continue
        elif row > 0:
            board[boss_x + row][boss_y + int(i[0]) - 10 * row] = i[1]
        elif row == 0:
            board[boss_x + row][boss_y + int(i[0])] = i[1]
    return boss_x, boss_y
