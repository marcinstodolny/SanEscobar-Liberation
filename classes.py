def possible_classes(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    human = {
        "name": "Maciej",
        "health": 150,
        "weapon": "sword",
        "age": 99,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 15,
        "armor": 5,
    }

    dwarf = {
        "name": "dwarf",
        "health": 200,
        "weapon": "Axe",
        "age": 42,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 12,
        "armor": 7,
    }

    elf = {
        "name": "elf",
        "health": 100,
        "weapon": "sword",
        "age": 442,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 19,
        "armor": 5,
    }
    return human, dwarf, elf
