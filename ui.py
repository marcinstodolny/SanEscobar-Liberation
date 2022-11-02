def display_board(board):
    for item in board:
        print(" ".join(item))


def display_items(items_list):
    for key,value in items_list.items():
        print(f"{key} : {value}")


def display_classes(players):
    for counter, classes in enumerate(players, start=1):
        print(f"{counter} - {classes['name']}")