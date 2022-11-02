def possible_classes(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    player = {
        "name": "Maciej",
        "weapon": "sword",
        "age": 99,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "live": 100,
        "dmg": 5,
        "armor": 5,
    }

    dwarf = {
        "name": "dwarf",
        "weapon": "Axe",
        "age": 42,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 100,
        "dmg": 5,
        "armor": 5,
    }

    elf = {
        "name": "elf",
        "weapon": "sword",
        "age": 442,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 200,
        "dmg": 5,
        "armor": 5,
    }
    return player, dwarf, elf
