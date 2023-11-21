import random
import json
    
    

class player():
    def mainmap(self):
        bigmap = [[["Junk Junction"],[],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
            [["Hanted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
            [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
            [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[],['Racing Course']],
            [['You fell in water'],['Viking Hill'],[],['Fatal Fields'],["Paradise Palms"],[]],
            [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[]]]
        return bigmap
    
    def __init__(self):
        whereto =  input("Where would you like to go?")
        inventory = []
        mats = {}
    
        
class opponent():
    
    def __init__(self):
        kind = {'bot':10,'noob':1,'sweat': 90,'casual': 50,'ninja':100,'child':25}
    
        opp,skill = random.choice(list(kind.items()))
        
        print(opp,skill)
        

class chest():
    rarities = ['common','uncommon','rare','epic','legendary']
    weapons = ['pistol','shotgun','assault rifle','Sub-machine gun','Sniper','grenade launcher']

    def randitem(self):
        rarity = random.choices(self.rarities,weights=(35,25,10,5,1))
        weapon = random.choices(self.weapons)

        return {weapon:rarity}
    
    def __init__(self):
        self.randitem(self)

opponent()

m