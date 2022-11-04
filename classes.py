def possible_classes(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    human = {
        "name": "Human",
        "weapon": "sword",
        "age": 99,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 150,
        "dmg": 15,
        "armor": 3,
    }

    Waszczykowski = {
        "name": "Waszczykowski",
        "weapon": "Axe",
        "age": 42,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 200,
        "dmg": 13,
        "armor": 4,
    }

    Soldier = {
        "name": "Soldier",
        "weapon": "sword",
        "age": 442,
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "health": 100,
        "dmg": 19,
        "armor": 2,
    }
    return human, Waszczykowski, Soldier
