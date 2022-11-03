def item():
    Dagger = {"name": "Dagger", "icon": "\U0001F5E1", "dmg": 2, "type": "dmg"}
    Pick = {"name": "Pick", "icon": "\U000026CF", "dmg": 1, "type": "dmg"}
    Wand = {"name": "Wand", "icon": "\U0000269A", "dmg": 3, "type": "dmg"}
    Shield = {"name": "Shield", "icon": "\u16D9", "armor": 1, "type": "armor"}
    potion = {"name": "Potion", "icon": "\u2764", "heal": 50, "type": "heal"}
    return [Dagger, Pick, Wand], [Shield], [potion]
