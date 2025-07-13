class Item:
    def __init__(self, name, item_type, health=0, strength=0, mana=0, dodge=0):
        self.name = name
        self.type = item_type
        self.health = health
        self.strength= strength
        self.mana= mana
        self.dodge=dodge

    def __repr__(self):
        return f"{self.name} ({self.type}) → 'Health': {self.health}, 'Strength': {self.strength}, 'Mana': {self.mana}, 'Dodge': {self.dodge}"