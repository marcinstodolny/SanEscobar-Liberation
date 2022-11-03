def possible_classes(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    human = {
        "name": "Maciej",
        "health": 100,
        "weapon": "sword",
        "age": 99,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 5,
        "armor": 5,
    }

    dwarf = {
        "name": "dwarf",
        "health": 100,
        "weapon": "Axe",
        "age": 42,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 5,
        "armor": 5,
    }

    elf = {
        "name": "elf",
        "health": 200,
        "weapon": "sword",
        "age": 442,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "dmg": 5,
        "armor": 5,
    }
    return human, dwarf, elf
