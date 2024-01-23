import asyncio
import pygame
import time,random,tkinter
import playsound

bigmap = [[["Junk Junction"],[""],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
    [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
    [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
    [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[""],['Racing Course']],
    [['You fell in water'],['Viking Hill'],[""],['Fatal Fields'],["Paradise Palms"],[""]],
    [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[""]]]
picmap = {}






tex = 'You fell in water'
rarities = ["white","green","blue","purple","yellow"]

while tex=='You fell in water':
    randx = random.randint(0,5)
    randy = random.randint(0,5)
    tex = bigmap[randx][randy][0]

print(tex)
x = randx
y = randy
loc = bigmap[x][y]

screen = pygame.display.set_mode((1280, 720))
chest = False
bg = "#98FB98"
color1 = "white"

        

async def t2():
    global screen,chest
    tally = 0
    while True:
        tally += 1

        if tally >= 3:
            if chest == False:
                chest = True
                
                tally = 0
                

        await asyncio.sleep(1)
    

async def t1():
    global bigmap,x,y,tex,loc,screen,chest,bg,rarities,color1
    pygame.init()
    clock = pygame.time.Clock()
    chestspawn = False
    enemyspawn = True
    running = True
    
    ches = pygame.image.load('chest.png')
    ches.convert()
    crect = ches.get_rect()
    crect.center = (random.randint(50,1230) , random.randint(50,670))
    picmap1=[]
    for i in picmap:
        picmap1.append(print(picmap[i]))


    if loc in picmap1:
        picture = {picmap[loc]}
    else:
        picture = "junk.png"

    map = pygame.image.load(picture)
    map.convert()
    map1 = map.get_rect()
    map1.center = (1280/2, 720/2)






    gun = pygame.image.load('gun1.png')
    gun.convert()
    gun1 = gun.get_rect()
    gun1.center = (1280/2 , 605 )

    enemy = {'bot':200,'noob':250,'sweat': 500,'casual': 450,'ninja':600,'child':400}

    skill = random.choices(list(enemy.items()),weights=(40,10,10,25,2,13))[0][1]
    esize = skill/5
    ehealth = esize
    varx = random.randint(-1,0)
    if varx == 0:
        varx = 1
    varx = varx*skill

    vary = random.randint(-1,0)
    if vary == 0:
        vary = 1
    vary = vary*skill
    
    dt = 0
    print("run")
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    enemy_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
    ihealth = ehealth
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(tex, True, '#ccffff', 'black')
        textRect = text.get_rect()
        textRect.center = (1280 // 2, 100 // 2)
        
        screen.fill(bg)
        
        screen.blit(map,map1)
        
        screen.blit(text, textRect)
        
       

        #gun background
        pygame.draw.rect(screen,color1,pygame.Rect((1280/2)-50, 550, 100, 100))
        screen.blit(gun,gun1) 

        if enemyspawn == True:
            pygame.draw.circle(screen, "red", enemy_pos, esize)
        pygame.draw.circle(screen, "blue", player_pos, 40)
        

        # enemy position
        enemy_pos.x += varx * dt
        enemy_pos.y += vary * dt 

        if enemy_pos.x > 1280:
            
            varx = -varx
        if enemy_pos.y > 720:
            
            vary = -vary
        if enemy_pos.x < 0:
            
            varx = -varx
        if enemy_pos.y < 0:
            
            vary = -vary

        if enemyspawn == True:
            
            pygame.draw.rect(screen,"green",pygame.Rect(enemy_pos.x-(ihealth/2), enemy_pos.y-100,ihealth , 10))
            pygame.draw.rect(screen,"red",pygame.Rect(enemy_pos.x-(ihealth/2)+ehealth, enemy_pos.y-100, ihealth-ehealth, 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 500 * dt
            if player_pos.y < 0:
                
                if x != 0:
                    x-=1 

                if chest:
                    chestspawn = True
                    chest = False

                loc = bigmap[x][y]
                player_pos.y = 720
                if random.randint(1,3) == 1:
                    enemyspawn = True

        if keys[pygame.K_s]:
            player_pos.y += 500 * dt
            if player_pos.y > 720:
      
                if x!=5: 
                    x+=1
                
                if chest:
                    chestspawn = True
                    chest = False

                loc = bigmap[x][y]
                player_pos.y = 0
                if random.randint(1,3) == 1:
                    enemyspawn = True

        if keys[pygame.K_a]:
            player_pos.x -= 500 * dt
            if player_pos.x < 0:
        
                if y!= 0:
                    y-=1

                if chest:
                    chestspawn = True
                    chest = False
                    
                loc = bigmap[x][y]
                player_pos.x = 1280
                if random.randint(1,3) == 1:
                    enemyspawn = True


        if keys[pygame.K_d]:
            player_pos.x += 500 * dt
            
            if player_pos.x > 1280:
            
                if y!= 5:
                    y+=1
                    
                if chest:
                    chestspawn = True
                    chest = False

                loc = bigmap[x][y]
                player_pos.x = 0
                if random.randint(1,3) == 1:
                    enemyspawn = True


        if event.type == pygame.MOUSEBUTTONUP:
            playsound.playsound("scar.mp3",block=False)
            mouse = pygame.mouse.get_pos()
            #pos = mouse position(x,y)
            #enemy_pos = center dot
            #esize = radius
            if ((mouse[0]-enemy_pos.x)**2 + (mouse[1]-enemy_pos.y)**2)**0.5 <= esize+5:
                ehealth -= (rarities.index(color1)+1)*5
                print(ehealth)

            if ehealth < 0:
                if enemyspawn == True:
                    playsound.playsound("fortdeath.mp3",block=False)
                    enemyspawn = False
                    skill = random.choices(list(enemy.items()),weights=(40,10,10,25,2,13))[0][1]
                    esize = skill/5
                    ehealth = esize
                    

        #enemy colision detection
        if ((player_pos.x + (esize-10) < enemy_pos.x and player_pos.x - (esize - 10) > enemy_pos.x) or (player_pos.x + (esize-10) > enemy_pos.x and player_pos.x - (esize-10) < enemy_pos.x)) and ((player_pos.y + (esize-10) < enemy_pos.y and player_pos.y - (esize-10) > enemy_pos.y) or (player_pos.y + (esize-10) > enemy_pos.y and player_pos.y - (esize-10) < enemy_pos.y)):
            if enemyspawn == True:
                
                screen.fill("black")

                font = pygame.font.Font('freesansbold.ttf', 50)
                text = font.render("You Died", True, 'red', 'black')
                textRect = text.get_rect()
                textRect.center = (1280 // 2, 720 // 2)
                screen.blit(text, textRect)

                pygame.display.flip()
                playsound.playsound("brutalized.mp3")
                exit()
            
        #chest colision detection
        if chestspawn:
            chest = False
            if ((player_pos.x + 50 < crect.center[0] and player_pos.x - 50 > crect.center[0]) or (player_pos.x + 50 > crect.center[0] and player_pos.x - 50 < crect.center[0])) and ((player_pos.y + 50 < crect.center[1] and player_pos.y - 50 > crect.center[1]) or (player_pos.y + 50 > crect.center[1] and player_pos.y - 50 < crect.center[1])):
                playsound.playsound("shortchest.mp3",block=False)
                chestspawn = False
                crect.center = (random.randint(50,1230) , random.randint(50,670))
                ran = random.choices(rarities,weights=(35,25,20,14,6))[0]

                if rarities.index(color1)< rarities.index(ran):
                    color1 = ran

            else:
                screen.blit(ches,crect)

        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        tex = f'{loc[0]}'
        if loc[0] == 'You fell in water':
            exit()
        await asyncio.sleep(0)

    pygame.quit()

async def main():
    tasks = []
    tasks.append( asyncio.create_task(t1()))
    tasks.append( asyncio.create_task(t2()))
    


    for i in range(len(tasks)):
            await(tasks[i])

asyncio.run(main())