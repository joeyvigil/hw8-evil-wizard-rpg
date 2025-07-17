from math import floor
import random
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
        
        self.gold=0
        self.max_health = health
        self.max_mana=mana
        self.weapon =Item("No Weapon", "Weapon")
        self.helmet =Item("No Helmet", "Helmet")
        self.armor = Item("No Armor", "Armor")
        self.shoes=Item("No Shoes", "Shoes")
    
    
    def attack(self,opponent):
        die=random.randint(1,100)
        print(f"dodge roll = {die}, required roll <= {opponent.dodge}")
        if (die > opponent.dodge):
            opponent.health -= self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength
            print(f"{self.name} has attacked {opponent.name} with {self.weapon.name} for {self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength} points of damage")
            print(f"{opponent.name} health = {opponent.health}")
        else:
            print(f"{opponent.name} has dodged")

    
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
        mana_cost=20
        if(self.mana-mana_cost>=0):
            opponent.health -=int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)
            self.mana-=mana_cost
            print(f"{self.name} has attacked {opponent.name} with 'spell: Throw Stone' for {int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)} points of damage")
            print(f"{opponent.name} health = {opponent.health}")
            print(f"mana cost: {mana_cost}, current mana {self.mana}")
        else:
            print("you dont have enough mana")
            
    def return_stats(self):
        stats = {'name': self.name, 
            'race': self.race,
            'class': self.classa,
            'health': self.health,
            'strength': self.strength,
            'mana': self.mana,
            'dodge':self.dodge,
            'gold':self.gold,
            'max_health': self.max_health,
            'weapon': self.weapon,
            'helmet': self.helmet,
            'armor': self.armor,
            'shoes': self.shoes
        }
        return stats
    
    def regenerate(self):
        pass #by default, you dont regenerate
    
    def full_mana(self):
        self.mana = self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana
        print(f"mana is now: {self.mana}/{self.mana}")
        
    def full_health(self):
        self.health = self.max_health+self.weapon.health+self.helmet.health+self.armor.health+self.shoes.health
        print(f"mana is now: {self.health}/{self.health}")


#child class            
class Fighter(Character):
    '''Fighter (20% chance to double strike, +40hp, +4 strength, +3 dodge)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race, 'Fighter', health+40, strength+4, mana, dodge+3)
        
    def attack(self,opponent):
        die=random.randint(1,100)
        print(f"dodge roll = {die}, required roll <= {opponent.dodge}")
        if (die > opponent.dodge):
            if(random.random()<.2):
                print("Double Strike!")
                opponent.health -= (self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength)*2
                print(f"{self.name} has attacked {opponent.name} with {self.weapon.name} for {(self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength)*2} points of damage")
                print(f"{opponent.name} health = {opponent.health}")
            else:
                opponent.health -= self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength
                print(f"{self.name} has attacked {opponent.name} with {self.weapon.name} for {self.strength+self.weapon.strength+self.helmet.strength+self.armor.strength+self.shoes.strength} points of damage")
                print(f"{opponent.name} health = {opponent.health}")
        else:
            print(f"{opponent.name} has dodged")
            
    def spell(self, opponent):
        #similar to attacking but cant dodge and cost mana
        mana_cost=20
        if(self.mana-mana_cost>=0):
            opponent.health -=int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)
            self.mana-=mana_cost
            print(f"{self.name} has attacked {opponent.name} with 'spell: Iron Resolve' for {int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)} points of damage")
            print(f"{opponent.name} health = {opponent.health}")
            print(f"mana cost: {mana_cost}, current mana {self.mana}")
        else:
            print("you dont have enough mana")

        
class Mage(Character):
    '''Mage (1.5x spell damage, +60 mana, +3 dodge)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race,'Mage', health, strength, mana+60, dodge+3)
        
    def spell(self, opponent):
        #similar to attacking but cant dodge and cost mana
        mana_cost=30
        if(self.mana-mana_cost>=0):
            opponent.health -=int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.45)
            self.mana-=mana_cost
            print(f"{self.name} has attacked {opponent.name} with 'spell: Arcane Bolt' for {int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.45)} points of damage")
            print(f"{opponent.name} health = {opponent.health}")
            print(f"mana cost: {mana_cost}, current mana {self.mana}")
        else:
            print("you dont have enough mana")


class Barbarian(Character):
    '''Barbarian (regenerates health after attacking, +80hp, +6 strength, -20 mana)'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race,'Barbarian', health+80, strength+6, mana-20, dodge)
        
    def spell(self, opponent):
        #similar to attacking but cant dodge and cost mana
        mana_cost=20
        if(self.mana-mana_cost>=0):
            opponent.health -=int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)
            self.mana-=mana_cost
            print(f"{self.name} has attacked {opponent.name} with 'spell: Crushing Blow' for {int((self.max_mana+self.weapon.mana+self.helmet.mana+self.armor.mana+self.shoes.mana)*.3)} points of damage")
            print(f"{opponent.name} health = {opponent.health}")
            print(f"mana cost: {mana_cost}, current mana {self.mana}")
        else:
            print("you dont have enough mana")
            
    def regenerate(self):
        self.health+= int((self.max_health)*.01)
        print(f"{self.name} regenerates {int((self.max_health)*.01)} current health: {self.health}")

class Enemy(Character):
    '''Enemy class'''
    def __init__(self, name, race, health, strength, mana, dodge):
        super().__init__(name, race, health, strength, mana, dodge+3)
        
    def regenerate(self):
        self.health+= int((self.max_health)*.01)
        print(f"{self.name} regenerates {int((self.max_health)*.01)} current health: {self.health}")