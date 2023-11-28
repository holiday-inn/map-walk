import random
import time
import pygame
    
class opponent:      
    def __init__(self):
        global kills
        kind = {'bot':10,'noob':1,'sweat': 90,'casual': 50,'ninja':99,'child':25}

        opp,skill = random.choices(list(kind.items()),weights=(40,10,10,25,2,13))[0]
        
        print(f'A wild {opp} has appeared')
        time.sleep(2)
        invalue = 0

        for i in inv.values():
            if i > invalue:
                invalue = i
            else:
                invalue += i/3
        
        if invalue-skill+(random.randint(-20,20)) > 0:
            print("You won!")
            kills += 1
            print(f"You have {kills} kills")

        else:
            print("You died")
            exit()
            
         

class chest:
    def randitem(self):
        rarities = ['\033[1mCommon\033[0m','\033[1;32;40mUncommon\033[0m','\033[1;34;40mRare\033[0m','\033[1;35;40mEpic\033[0m','\033[1;33;40mLegendary\033[0m']
        values = [20,40,60,80,100]

        rarity = random.choices(rarities,weights=(35,25,20,14,6))[0]
        value = values[rarities.index(rarity)]
        print(f"You found a {rarity} gun in a chest!")
        return [rarity,value]


    
    def __init__(self):
        pass
    
def bmap():
        bigmap = [[["Junk Junction"],[""],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
            [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
            [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
            [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[""],['Racing Course']],
            [['You fell in water'],['Viking Hill'],[""],['Fatal Fields'],["Paradise Palms"],[""]],
            [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[""]]]
        return bigmap

def main():
    map = bmap()
    continued = True
    while continued == True:
        drop = input("Where we droppin boys?: ")
        while True:
            try:
                for row in map:
                    for j in row:
                        k = j[0]
                        
                        if drop == k:
                            continued = False
                            print("Location found")
                            x = map.index(row)
                            y = row.index(j)
                
                break
                
            except:
                pass


    loc = map[x][y]

    
    global inv
    global kills
    inv = {'Pickaxe':10}
    kills = 0
    limit = False

    while True:
        print(f"You are now in {loc[0]}")
        chestloot = False
        chance = random.randint(1,2)

        if chance == 1 and limit == False:
            loot = chest().randitem()
            chestloot = True


        elif chance == 2 and limit == False:
            opponent()

        to =  input("\n>")

        limit = False
        
        if kills == 6+ random.randint(1,7):
                print("You won!")
                exit()
        
        elif to == 'get' :
            if chestloot == True:
                inv[loot[0]] = loot[1]

                print("Your inventory is: ",end=' ')

                for i in inv:
                    if i == "Pickaxe":
                        print(i,end=", ")

                    elif list(inv.keys())[-1] == i:
                        print(f"and {i} Gun")

                    else:
                        print(i, end = " Gun, ")  
                print("\n")
            else:
                print("You can't do that")
                limit = True

        elif to == 'n' :
            if x == 0:
                print("You can't walk off the map")
            else:
                x-=1 
                if map [x][y] == [""]: x-=1


        elif to == "e" :
            if y ==5:
                print("You can't walk off the map")
            else:
                y+=1
                if map [x][y] == [""]: y+=1

        elif to == 's' :
            if x == 5:
                print("You can't walk off the map")
            else: 
                x+=1
                if map [x][y] == [""]: x+=1

        elif to == "w" :
            if y ==0:
                print("You can't walk off the map")
            else:
                y-=1
                if map [x][y] == [""]: y-=1
    
        
        
        loc = map[x][y]
        if loc[0] == 'You fell in water':
            print('You fell in water')
            exit()

        
        




            
             

main()