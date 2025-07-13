from item_class import Item

class Character:
    def __init__(self, name, race, classa, health, strength, mana, dodge):
        self.name = name
        self.race = race
        self.classa= classa
        
        self.health = health
        self.strength = strength
        self.mana= mana
        self.dodge=dodge
        
        self.max_health = health
        self.weapon =Item("No Weapon", "Weapon")
        self.helmet =Item("No Helmet", "Helmet")
        self.armor = Item("No Armor", "Armor")
        self.shoes=Item("No Shoes", "Shoes")
    
    
    def attack(self,opponent):
        opponent.health -= self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength
        print(f"{self.name} has attacked {opponent.name} with {self.weapon.name} for {self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength} points of damage")
        if opponent.health <=0:
            print(f"{opponent.name} has perished")
        else:
            print(f"{opponent.name} has {opponent.health} health left")
    
    def equip(self,item):
        if item.type=='Weapon':
            self.weapon=item
        if item.type=='Helmet':
            self.helmet=item
        if item.type=='Armor':
            self.armor=item
        if item.type=='Shoes':
            self.shoes=item
        print(f"{self.name} has equipped {item}")
            
    def spell(self, opponent):
        #similar to attacking but cant dodge and cost mana
        pass
            
    def return_stats(self):
        stats = {
            'name': self.name, 
            'race': self.race,
            'class': self.classa,
            'health': self.health,
            'strength': self.strength,
            'mana': self.mana,
            'dodge':self.dodge,
            'max_health': self.max_health,
            'weapon': self.weapon,
            'helmet': self.helmet,
            'armor': self.armor,
            'shoes': self.shoes
        }
        return stats


#child class            
class Fighter(Character):
    '''Fighter (20% chance to double strike, +40hp, +4 strength, +3 dodge)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race, 'Fighter', health+40, strength+4, mana, dodge+3)
        
    def attack(self,opponent):
        opponent.health -= self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength
        print(f"{self.name} has attacked {opponent.name} with {self.weapon.name} for {self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength} points of damage")
        if opponent.health <=0:
            print(f"{opponent.name} has perished")
        else:
            print(f"{opponent.name} has {opponent.health} health left")
        
class Mage(Character):
    '''Mage (1.5x spell damage, +60 mana, +3 dodge)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race,'Mage', health, strength, mana+60, dodge+3)
        
    def attack(self, opponent):
        opponent.health -= self.strength
        print(f"{self.name} has attacked {opponent.name} with a FireBall! for {self.strength} points of damage")
        if opponent.health <=0:
            print(f"{opponent.name} has perished")
        else:
            print(f"{opponent.name} has {opponent.health} health left")

class Barbarian(Character):
    '''Barbarian (regenerates health after attacking, +80hp, +6 strength, -20 mana)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race,'Barbarian', health+80, strength+6, mana-20, dodge)
        
    def regenerate(self):
        self.health+= 5
        print(f"{self.name} regenerates 5 health. current health: {self.health}")

class Enemy(Character):
    '''Enemy class'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race, health+40, strength+4, mana, dodge+3)
        
    def regenerate(self):
        self.health+= 5
        print(f"{self.name} regenerates 5 health. current health: {self.health}")