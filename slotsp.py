import pygame
import time,asyncio,random

symbols = ['JACKPOT',"Grapes",'Orange',"Lemon","Cherry","7",'JACKPOT',"Grapes"]
pictures = {'JACKPOT':"gun1.png","Grapes":"gun1.png",'Orange':"gun1.png","Lemon":"gun1.png","Cherry":"gun1.png","7":"gun1.png",'JACKPOT':"gun1.png","Grapes":"gun1.png"}
screen = pygame.display.set_mode((1280, 720))
color = "purple"
tally = 0

async def p1():
    global screen,color,tally
    print("here")
    pygame.init()
    symbols = ['JACKPOT',"Grapes",'Orange',"Lemon","Cherry","7",'JACKPOT',"Grapes"]
    biglis = []
    for i in range(3):
        selec = random.randint(0,5)
        var = [symbols[selec],symbols[selec+1],symbols[selec+2]]
        biglis.append(var)
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill(f"{color}")
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render(f"{biglis}", True, '#ccffff', 'black')
        textRect = text.get_rect()
        textRect.center = (1280 // 2, 100 // 2)
        # RENDER YOUR GAME HERE
        screen.blit(text,textRect)

        for i in biglis:
            for j in i:
                gun = pygame.image.load(pictures[j])
                gun.convert()
                gun1 = gun.get_rect()
                gun1.center = (1280/2 , 605 )
                screen.blit(gun, gun1)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    
        await asyncio.sleep(0)
    pygame.quit()

async def p2():
    global screen,color,tally
    while True:
        if tally%4 <2:
            print("goo")
            color = "blue"
        else: color = "purple"
        tally +=1
        await asyncio.sleep(1) 


async def main():
    tasks = []
    tasks.append(asyncio.create_task(p1()))
    tasks.append(asyncio.create_task(p2()))

    for i in range(len(tasks)):
            await(tasks[i])

asyncio.run(main()) 