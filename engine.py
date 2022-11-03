import random
import enemies
import story
import ui
import util
from time import sleep
ITEMS_MEANING = {"\U000026CF": "Pick", "\u16D9": "Wand", "\u26E8": "Shield", "\U000026B8": "Sword", "\u2764":"Potion"}
DMG_ITEMS = {"Sword": 2, "Wand": 3, "Axe": 1}
ARMOR_ITEMS = {"Shield": 1}
HEALTH_ITEMS = {"Potion": 50}
ENEMIES = ["\u2620"]



def create_board(width, height, BOARD_BORDER):
    return [
        [
            BOARD_BORDER if check_border(height, j) or check_border(width, i) else " "
            for i in range(width)
        ]
        for j in range(height)
    ]


def check_border(direction, iterator):
    return iterator in [0] + [direction - k for k in [0, 1]]


def put_player_on_board(board, player):
    print(player["x"], player["y"])
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
        if board[x][y] not in [player["icon"], BOARD_BORDER] + list(ITEMS_MEANING.keys()) + ENEMIES:
            board[x][y] = random.choice(ENEMIES)
        else:
            enemies_number += 1

def king(king_icon,key, board, player):
    if board[player["x"]][player["y"]] == king_icon and count_enemies(board) > 0:
        print("You have to defeat all enemies to reach the next level")
        if key == "s":
            player["x"] -=1
        elif key == "d":
            player["y"] -= 1

def count_enemies(board):
    return sum(row.count(ENEMIES[0]) for row in board)

def player_movement(board, player, key, collected_items, BOARD_BORDER, king_icon,boards):
    if key == "s" and board[player["x"] + 1][player["y"]] != BOARD_BORDER:
        player["x"] += 1
        king(king_icon,key, board, player)

    if key == "w" and board[player["x"] - 1][player["y"]] != BOARD_BORDER:
        player["x"] -= 1
    if key == "a" and board[player["x"]][player["y"] - 1] != BOARD_BORDER:
        player["y"] -= 1
    if key == "d" and board[player["x"]][player["y"] + 1] != BOARD_BORDER:
        player["y"] += 1
        king(king_icon,key, board, player)
    item_enemy_check(board, player, collected_items)
    if board[player["x"]][player["y"]] == "\u2591":
        board, boards = change_board(player, boards)
    if len(boards) == 1:
        boss_battle_check(board, player, collected_items)
    return board, boards


def change_board(player, boards):
    print(len(boards))
    boards = boards[1:]
    print(len(boards))
    player["x"] = 2
    player["y"] = 1
    return boards[0], boards
    
def boss_battle_check(board, player, collected_items):
    location = board[player["x"]][player["y"]]
    if location not in [" ", "#"]:
        fight_with_enemy(player, enemies.boss(player["name"]))
        ui.hall_of_fame(collected_items)
        story.outro(player["name"])


def item_enemy_check(board, player, collected_items):

    location = board[player["x"]][player["y"]]
    if location in list(ITEMS_MEANING.keys()):
        item = ITEMS_MEANING[location]
        if item in collected_items:
            collected_items[item] += 1
        else:
            collected_items[item] = 1
        equipment_to_stats(item, player)
    elif location in ENEMIES:
        fight_with_enemy(player)



def equipment_to_stats(item, player):
    if item in list(DMG_ITEMS.keys()):
        player["dmg"] += DMG_ITEMS[item]
    elif item in list(ARMOR_ITEMS.keys()):
        player["armor"] += ARMOR_ITEMS[item]
    elif item in list(HEALTH_ITEMS.keys()):
        player["health"] += HEALTH_ITEMS[item]


def fight_with_enemy(player, boss=False):
    if boss:
        enemy = boss
        fight = [player, boss]
    else:
        enemy = random.choice(enemies.possible_classes())
        fight = [player, enemy]
    current_round = 0
    util.clear_screen()
    enemies_picture = story.enemies_list()
    while enemy["health"] > 0:
        print(enemies_picture[enemy["name"]])
        current_player = fight[current_round % 2]
        current_enemy = fight[(current_round+1) % 2]
        damage = random_damage(current_player)
        if  damage - current_enemy["armor"] > 0:
            current_enemy["health"] -= damage - current_enemy["armor"]
            ui.show_dmg(current_player, current_enemy, damage, current_enemy["armor"])
            sleep(0.25)
            ui.health_level(player, enemy, current_player)
        else:
            ui.show_dmg(current_player, current_enemy, damage, current_enemy["armor"])
        sleep(1)  
        current_round += 1
        util.clear_screen() 

def random_damage(player):
    return random.randint(int(player["dmg"]*0.5), int(player["dmg"]*1.5))

def boss_coordinates(boss_x, boss_y):
    boss_x += random.randint(-1,1)
    boss_y += random.randint(-1,1)
    if boss_x > 12:
        boss_x = 11
    elif boss_x < 3:
        boss_x = 4
    if boss_y > 20:
        boss_y = 19
    elif boss_y < 3:
        boss_y = 4
    return boss_x,boss_y

def boss_movement(board, boss_x_input, boss_y_input):
    boss_x,boss_y = boss_x_input, boss_y_input
    row = 0
    for i in enumerate(story.small_boss):
        if i[1] == "\n":
            row += 1
            continue
        elif row > 0:
            board[boss_x + row][boss_y + int(i[0])-10*row] = " "
        elif row == 0:
            board[boss_x + row][boss_y + int(i[0])] = " "
    boss_x,boss_y = boss_coordinates(boss_x_input,boss_y_input)
    row = 0
    for i in enumerate(story.small_boss):
        if i[1] == "\n":
            row += 1
            continue
        elif row > 0:
            board[boss_x + row][boss_y + int(i[0])-10*row] = i[1]
        elif row == 0:
            board[boss_x + row][boss_y + int(i[0])] = i[1]
    return boss_x, boss_y