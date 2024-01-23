import pygame
import asyncio
import random
import time

bigmap = [[["Junk Junction"],[""],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
    [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
    [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
    [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[""],['Racing Course']],
    [['You fell in water'],['Viking Hill'],[""],['Fatal Fields'],["Paradise Palms"],[""]],
    [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[""]]]

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
dt = 0
ltim = time.time() + (random.randint(1,5))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fill = '#ccffff'
tex = 'Loot Lake'
x = 1
y = 2
loc = bigmap[x][y]
img = pygame.image.load('kidfort.PNG')
img.convert()
rect = img.get_rect()

ches = pygame.image.load('chest (1).png')
ches.convert()
crect = ches.get_rect()
crect.center = (random.randint(50,1000) // 2, random.randint(50,600) // 2)
bg_img = pygame.image.load('Fornie.PNG')
bg_img = pygame.transform.scale(bg_img,(width,height))
inv = {'Pickaxe':10}

def randitem():
        rarities = ['\033[1mCommon\033[0m','\033[1;32;40mUncommon\033[0m','\033[1;34;40mRare\033[0m','\033[1;35;40mEpic\033[0m','\033[1;33;40mLegendary\033[0m']
        values = [20,40,60,80,100]

        rarity = random.choices(rarities,weights=(35,25,20,14,6))[0]
        value = values[rarities.index(rarity)]
        print(f"You found a {rarity} gun in a chest!")
        return [rarity,value]

async def t1():
    global bigmap,running,screen,clock,dt,fill,tex,x,y,loc,player_pos,img,rect,crect,ches,height,width,bg_img,inv,randitem
    
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last fram
        screen.blit(bg_img,(0,0))
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(tex, True, '#ccffff', 'black')
        textRect = text.get_rect()
        textRect.center = (1280 // 2, 100 // 2)
        
        screen.blit(text, textRect)
        rect.center = player_pos
        screen.blit(img, rect)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            player_pos.y -= 600 * dt
            
            if player_pos.y < 0:
                if x != 0:
                    x-=1 

                loc = bigmap[x][y]
                player_pos.y = 720


        if keys[pygame.K_s]:
            player_pos.y += 600 * dt
            if player_pos.y > 720:
                if x!=5: 
                    x+=1

                loc = bigmap[x][y]
                player_pos.y = 0
 
                

        if keys[pygame.K_a]:
            player_pos.x -= 600 * dt
            if player_pos.x < 0:
                if y!= 0:
                    y-=1

                loc = bigmap[x][y]
                player_pos.x = 1280

                
        if keys[pygame.K_d]:
            player_pos.x += 600 * dt
            
            if player_pos.x > 1280:
                if y!= 5:
                    y+=1

                loc = bigmap[x][y]
                player_pos.x = 0

        tex = f'{loc[0]}'
        if loc[0] == 'You fell in water':
            exit()
                
        await asyncio.sleep(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
 
        
async def t2():
    global ches,crect,screen
    
    while True:
        await asyncio.sleep(random.randint(1,10))
        screen.blit(ches,crect)
        print("chest spawns")

 

async def t3():
    while True:
        await asyncio.sleep(random.randint(1,10))


    
async def main():
    await asyncio.gather(t1(),t2())

asyncio.run(main())
    
pygame.quit()