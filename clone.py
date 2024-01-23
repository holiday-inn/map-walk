import pygame
import time,asyncio
import random
import copy

color = "white"
symbols = ['JACKPOT',"Grapes",'Orange',"Lemon","Cherry","7",'JACKPOT',"Grapes",'Orange',"Lemon","Cherry","7"]
pictures = {'JACKPOT':"jackpot.png","Grapes":"grapes.png",'Orange':"orange.png","Lemon":"lemon.png","Cherry":"cherry.png","7":"7.png",'JACKPOT':"jackpot.png","Bluberry":"Grapes.png"}
money = 100
timer = 0
multi = 1
make = False

async def p1():
    global money,multi,timer,make
    
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    iteration = 0
    simp_pos = []
    ches = []
    speed = []   
    position = []
    sort_pos = []
    switch = False 
    imagelist = []
    thing = 0
    sped = 31.05

    for j in range(3):
        off = random.randint(0,5)
        for i in range(0,5):
            position.append(j)
            speed.append(0)
            imagelist.append(pictures[symbols[i+off]])
    
            ches.append(pygame.image.load(pictures[symbols[i+off]]))
            simp_pos.append(pygame.Vector2(500+(j*200) / 2, screen.get_height()+(220*i) / 2))
    
    
    copycopy = speed.copy()

    

    while running:
        result = []
        width = screen.get_width() 
        height = screen.get_height()
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            
            mouse = pygame.mouse.get_pos() 
            if switch ==  False:
                if width/2-110 <= mouse[0] <= width/2+30 and 600 <= mouse[1] <= 660:
                        if (money - 20) >= 0:
                            money -= 20
                            switch = True
                            thing +=1
                            iteration = 0
                            
                            if thing>1:
                                ches = newches
                                imagelist = newimagelist
                
    
        if switch == True:
            for i in simp_pos:
                print(speed)
                iteration+=1
                rand = speed[simp_pos.index(i)]
                if iteration:
                    speed[0] = sped
                    speed[1] = sped
                    speed[2] = sped
                    speed[3] = sped
                    speed[4] = sped

                elif iteration == 1000:
                    speed[5] = sped
                    speed[6] = sped
                    speed[7] = sped
                    speed[8] = sped  
                    speed[9] = sped 

                elif iteration == 2000:
                    speed[10] = sped
                    speed[11] = sped
                    speed[12] = sped    
                    speed[13] = sped
                    speed[14] = sped

                    
                elif speed[simp_pos.index(i)] > 0:
                    speed[simp_pos.index(i)] -= 0.1

                    i.y += rand  
                
                elif speed[14]<0:
                    sort_pos = []
                    
                    for i in simp_pos:
                        sort_pos.append(i.y)
                        sort_pos.sort()
                        
                    midcord = sort_pos[7]

                    for i in simp_pos:
                        i.y+=385-midcord

                    numlist = [1,2,3,6,7,8,11,12,13]
                    for i in range(len(imagelist)):
                        if i in numlist:
                            result.append(imagelist[i])

                    print(result)    

                    if (result[0] == result[4] == result[8]) or (result[2] == result[4] == result[6]):
                        print("diagonal")
                        money += 100*multi
                        
                    if (result[0] == result[3]) or (result[6] == result[3]) or (result[0] == result[6]) :
                        print("2 of kind")
                        make = True
                    

                    elif (result[0] == result[3] == result[6]):
                        print("straight line")
                        if result[1] == 'jackpot.png':
                            print("jackpot")
                            money==500*multi
                        else:
                            money+= 20*multi
                        
                    speed = copycopy.copy()

                    newimagelist = []
                    newches = []

                    for j in range(3):
                        off = random.randint(0,5)
                        for i in range(0,5):
                            newimagelist.append(pictures[symbols[i+off]])
                            newches.append(pygame.image.load(pictures[symbols[i+off]]))


                    switch = False
                    break
        

                if i.y > 640:
                    i.y -= 540
                    #ches = pygame.image.load(random.choice(list(pictures.values())))
                
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill(color)

        
        for j in range(0,len(ches)):
            ches[j].convert()
            crect = ches[j].get_rect()
            crect.center = (simp_pos[j].x , (simp_pos[j].y))
            screen.blit(ches[j],crect)
            
        tex = f"Balance: {money}"
        if (money - 20) <0:tex = "no more money loser"
        pygame.draw.rect(screen,"white",pygame.Rect(0, 0, 1280, 230))
        pygame.draw.rect(screen,"white",pygame.Rect((0, 550, 1280, 200)))
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(tex, True, 'black', 'white')
        textRect = text.get_rect()
        textRect.center = ((1280/2) - 40,200)
        screen.blit(text,textRect)

        
        if make == True:
            text = font.render("+100", True, 'green')
            textRect = text.get_rect()
            textRect.center = (1280/2,600)
            screen.blit(text,textRect)
            


        mouse = pygame.mouse.get_pos()
        
        if width/2-110 <= mouse[0] <= width/2+30 and 600 <= mouse[1] <= 660: 
                pygame.draw.rect(screen,"#BB3F3F",[width/2-110,600,140,60]) 
          
        else: pygame.draw.rect(screen,"#FF000D",[width/2-110,600,140,60])

        text = font.render("SPIN", True, 'white')
        textRect = text.get_rect()
        textRect.center = ((1280/2) - 40,632)
        screen.blit(text,textRect)
        
        

        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
        await asyncio.sleep(0)

    pygame.quit()
    exit()
    

async def p2():
    global money,multi,timer,make
    
    while True:
        timer +=1
        frenzy = random.randint(1,4)
        make = False
        if timer == frenzy:
            multi = 2
            print("frenzy")
            if timer + 20 == frenzy:
                multi = 1
            
        money +=10
        await asyncio.sleep(1) 


async def main():
    tasks = []
    tasks.append(asyncio.create_task(p1()))
    tasks.append(asyncio.create_task(p2()))

    for i in range(len(tasks)):
            await(tasks[i])

asyncio.run(main()) 