def possible_classes(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    human = {
        "name": "Maciej",
        "weapon": "sword",
        "age": 99,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 150,
        "dmg": 15,
        "armor": 5,
    }

    dwarf = {
        "name": "Dwarf",
        "weapon": "Axe",
        "age": 42,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 150,
        "dmg": 50,
        "armor": 7,

    }

    elf = {
        "name": "Elf",
        "weapon": "sword",
        "age": 442,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 100,
        "dmg": 19,
        "armor": 5,
    }
    return human, dwarf, elf
