import random
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


def put_items_on_board(board, player):
    items_icon = ["+", "&", "$", "="]
    item_number = random.randint(5,10)
    for _ in range(item_number):
        x, y = random.randint(1,len(board)-1), random.randint(1,len(board[0])-1)
        if board[x][y] not in [player["icon"], "#"] + items_icon:
            board[x][y] = random.choice(items_icon)
        else:
            item_number += 1
            
            