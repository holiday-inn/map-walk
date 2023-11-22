import random
import json
    
    

class player:
    def map(self):
        bigmap = [[["Junk Junction"],[],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
            [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
            [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
            [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[],['Racing Course']],
            [['You fell in water'],['Viking Hill'],[],['Fatal Fields'],["Paradise Palms"],[]],
            [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[]]]
        return bigmap
    
    def __init__(self):
        map = self.map()

        drop = input("Where we droppin boys?: ")
        for row in map:
            for j in row:
                
                if j == []: j = ['']
                k = j[0]
                if drop == k:
                    print("Location found")
                    x = map.index(row)
                    y = row.index(j)
                    print(y,x)

                    
        while True:    
            loc = map[x][y]
            print(loc,x,y)
            lis = ['x+',['x-']]
            
            to =  input("Where would you like to go?: ")
            if  y == 5:
                pass
            if to == 'n':
                x-=1
                if map [x][y] == []: x-=1
            elif to == "e":
                y+=1
                if map [x][y] == []: y+=1
            elif to == 's':
                x+=1
                if map [x][y] == []: x+=1
            elif to == "w":
                y-=1
                if map [x][y] == []: y-=1
            elif to == "exit": break
                
            loc = map[x][y]


        inv = ['Pickaxe']
    
        
class opponent:
    def tip(opp,skill,ki):
        return None


    def __init__(self, inv):
        self.inv = inv
        kind = {'bot':10,'noob':1,'sweat': 90,'casual': 50,'ninja':99,'child':25}
        
        opp,skill = random.choice(list(kind.items()))
        if opp == 'bot':
            print('fight happening')
            roll = random.randint(1,100)
            if roll <= skill:
                print("eat doodoo")

            
        print(opp,skill)
        

class chest:
    
    #['\x1b[1mCommon\x1b[0m']
    #weapons = ['Pistol','Shotgun','Assault rifle','Sub-machine gun','Sniper','Grenade launcher']

    def randitem(self):
        rarities = ['Common','Uncommon','Rare','Epic','Legendary']
        values = [20,40,60,80,99]

        rarity = random.choices(rarities,weights=(45,35,14,4,2))
        print(rarity)
        
        value = values[rarities.index(rarity)]

        print(value)
        choice = input(f"Would you like to pickup the {rarity} gun?")


        while True:
            if choice == "Yes":
                return {rarity,value}
            
            elif choice == "No":
                return None
            
            else:
                print("That is not a valid input")
            
            break

    
    def __init__(self):
        self.randitem()
    

chest()
