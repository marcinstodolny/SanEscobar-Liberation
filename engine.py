import random

ITEMS_ICON = ["+", "&", "$", "="]
ITEMS_MEANING = {"+": "Sword", "&": "Wand", "$": "Shield", "=": "Axe"}

def create_board(width, height, BOARD_BORDER):
    return [
        [
            BOARD_BORDER
            if check_border(height, j)
            or check_border(width, i)
            else " "
            for i in range(width)
        ]
        for j in range(height)
    ]
    
def check_border(direction, iterator):
    return iterator in [0] + [
        direction - k for k in [0,1]
    ]


def put_player_on_board(board, player):
    print(player["x"], player["y"])
    for sub_list in board:
        if player["icon"] in sub_list:
            board[board.index(sub_list)][sub_list.index(player["icon"])] = " "
    board[player["x"]][player["y"]] = player["icon"]


def put_items_on_board(board, player, BOARD_BORDER):
    item_number = random.randint(5,10)
    for _ in range(item_number):
        x, y = random.randint(1,len(board)-1), random.randint(1,len(board[0])-1)
        if board[x][y] not in [player["icon"], BOARD_BORDER] + ITEMS_ICON:
            board[x][y] = random.choice(ITEMS_ICON)
        else:
            item_number += 1

def player_movement(board, player, key, collected_items,BOARD_BORDER):
    if key == 's' and board[player["x"]+1][player['y']] != BOARD_BORDER:
        player["x"] += 1
    if key == 'w' and board[player["x"]-1][player['y']] != BOARD_BORDER:
        player["x"] -= 1
    if key == 'a' and board[player["x"]][player['y'] - 1] != BOARD_BORDER:
        player["y"] -= 1
    if key == 'd' and board[player["x"]][player['y'] + 1] != BOARD_BORDER:
        player["y"] += 1
    item_check(board, player, collected_items)
    if board[player["x"]][player['y']] == "]":
        change_board(player)
    
def change_board(player):
    player["x"] = 2
    player['y'] = 1
    
    
def item_check(board, player, collected_items):
    location = board[player["x"]][player['y']]
    if location in ITEMS_ICON:
        if ITEMS_MEANING[location] in collected_items:
            collected_items[ITEMS_MEANING[location]] += 1
        else:
            collected_items[ITEMS_MEANING[location]] = 1