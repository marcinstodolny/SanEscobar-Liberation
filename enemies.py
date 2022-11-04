import story


def possible_classes():
    demon = {
        "name": "Demon",
        "health": 50,
        "dmg": 12,
        "armor": 3,
    }

    dinosaur = {
        "name": "Dinosaur",
        "health": 75,
        "dmg": 13,
        "armor": 3,
    }

    dragon = {
        "name": "Dragon",
        "health": 30,
        "dmg": 20,
        "armor": 2,
    }

    alien = {
        "name": "Alien",
        "health": 100,
        "dmg": 12,
        "armor": 1,
    }
    Lucifer = {
        "name": "Lucifer",
        "health": 50,
        "dmg": 15,
        "armor": 1,
    }
    Wyvern = {
        "name": "Wyvern",
        "health": 75,
        "dmg": 5,
        "armor": 5,
    }

    return [demon, dinosaur, dragon, alien, Lucifer, Wyvern]


def boss(player):
    story.story_final_boss(player)
    return {
        "name": "Boss",
        "health": 200,
        "dmg": 10,
        "armor": 0,
    }
