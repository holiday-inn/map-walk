import asyncio
import pygame
import time,random,tkinter,math
import playsound

bigmap = [[["Junk Junction"],["Grass"],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
    [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
    [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
    [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],["Grass"],['Racing Course']],
    [['Water'],['Viking Hill'],["Grass"],['Fatal Fields'],["Paradise Palms"],["Grass"]],
    [['Water'],['Water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],["Grass"]]]


def blitRotate(surf, image, origin, pivot, angle):
    image_rect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)



rarities = ["white","green","blue","purple","yellow"]

randx = random.randint(0,5)
randy = random.randint(0,5)
tex = bigmap[randx][randy][0]


x = randx
y = randy
loc = bigmap[x][y]

screen = pygame.display.set_mode((1280, 720))
chest = False
bg = "#98FB98"
color1 = "white"


potentialkills = [6,5,4,3,15,20]
needkills = random.choices(potentialkills,weights=(40,25,13,10,10,2))[0]

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
    global bigmap,x,y,tex,loc,screen,chest,bg,rarities,color1,needkills
    kills = 0
    pygame.init()
    clock = pygame.time.Clock()
    chestspawn = False
    enemyspawn = True
    running = True
    
    ches = pygame.image.load('chest.png')
    ches.convert()
    crect = ches.get_rect()
    crect.center = (random.randint(50,1230) , random.randint(50,670))


    map = pygame.image.load("junk.png")
    map.convert()
    map1 = map.get_rect()
    map1.center = (1280/2, 720/2)




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
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    enemy_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 3)
    ihealth = ehealth
    angle = 0
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(tex, True, 'Black','light blue')
        textRect = text.get_rect()
        textRect.center = (1280 // 2, 100 // 2)
        
        screen.fill(bg)
        
        screen.blit(map,map1)
        
        screen.blit(text, textRect)
        
        gun = pygame.image.load('gun1.png')
        gun.convert()
        gun1 = gun.get_rect()
        gun1.center = (1280/2,605)



        font = pygame.font.Font('freesansbold.ttf', 30)
        # pygame.draw.rect(screen,"red",pygame.Rect(enemy_pos.x-(ihealth/2)+ehealth, enemy_pos.y-100, ihealth-ehealth, 10))
        
        
        pygame.draw.rect(screen,"white",pygame.Rect(1050,40,200,90))
        
        text = font.render(f" {kills} ", True, 'black')
        textRect = text.get_rect()
        textRect.center = (1100,110)
        screen.blit(text, textRect)

        text = font.render(f" {needkills -kills} ", True, 'black')
        textRect.center = (1200,110)
        screen.blit(text, textRect)

        kill = pygame.image.load('killa (2).png')
        kill.convert()
        kill1 = kill.get_rect()
        kill1.center = (1100,70)
        screen.blit(kill,kill1)


        kill = pygame.image.load('pcounter.png')
        kill.convert()
        kill1 = kill.get_rect()
        kill1.center = (1200,70)
        screen.blit(kill,kill1)

        #gun background
        mouse = pygame.mouse.get_pos()

        dely = (player_pos.y-mouse[1])
        delx = (player_pos.x-mouse[0])
        if player_pos.x-mouse[0]!=0:
            angle = abs(math.degrees(math.atan((player_pos.y-mouse[1])/(player_pos.x-mouse[0]))))
        else:
            angle = 0
            
        if delx <0:
            if dely<0:angle = 360-angle 

        elif delx>0:
            gun = pygame.transform.flip(gun,False,True)
            #angle = -angle
            #3th quad
            if dely<0:angle = 180+angle
            #2st
            else:angle = 180-angle

        blitRotate(screen,gun,player_pos,[0,0],angle)




        if enemyspawn == True:
            pygame.draw.circle(screen, "red", enemy_pos, esize)
            joe2 = pygame.image.load('dvdlogo.PNG')
            joe2.convert()
            joe3 = gun.get_rect()
            joe3.center = enemy_pos
            screen.blit(joe2,joe3)
        pygame.draw.circle(screen, f"{color1}", player_pos, 40)

        joe = pygame.image.load('jonesy.PNG')
        joe.convert()
        joe1 = gun.get_rect()
        joe1.center = player_pos
        screen.blit(joe,joe1)

        

        # enemy position
        enemy_pos.x += varx * dt
        enemy_pos.y += vary * dt 

        if enemy_pos.x >= 1280:
            
            varx = -varx
        if enemy_pos.y >= 720:
            
            vary = -vary
        if enemy_pos.x <= 0:
            
            varx = -varx
        if enemy_pos.y <= 0:
            
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
            

         
            if ((mouse[0]-enemy_pos.x)**2 + (mouse[1]-enemy_pos.y)**2)**0.5 <= esize+5:
                ehealth -= (rarities.index(color1)+1)*5
             

            if ehealth < 0:
                if enemyspawn == True:
                    kills+=1
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

        if needkills<= kills:
            font = pygame.font.Font('freesansbold.ttf', 50)


            joe4 = pygame.image.load('vicro.png')
            joe4.convert()
            joe5 = gun.get_rect()
            joe5.center = (400,0)
            screen.blit(joe4,joe5)

            pygame.display.flip()
            playsound.playsound("victory-royale.mp3")
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