import story


def possible_classes():
    demon = {
        "name": "Demon",
        "health": 50,
        "dmg": 8,
        "armor": 3,
    }

    dinosaur = {
        "name": "Dinosaur",
        "health": 75,
        "dmg": 9,
        "armor": 3,
    }

    dragon = {
        "name": "Dragon",
        "health": 20,
        "dmg": 15,
        "armor": 2,
    }

    alien = {
        "name": "Alien",
        "health": 125,
        "dmg": 8,
        "armor": 3,
    }
    return [demon, dinosaur, dragon, alien]


def boss(player):
    story.story_final_boss(player)
    return {
        "name": "Boss",
        "health": 200,
        "dmg": 10,
        "armor": 0,
    }
