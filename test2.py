import pygame
import asyncio

bigmap = [[["Junk Junction"],[""],["Motel"],["Lazy Links"],["River"],["Risky Reels"]],
    [["Haunted Hills"],["Pleasant Park"],["Loot Lake"],["River"],["Tomato Town"],["Wailing Woods"]],
    [['Abandoned Forest'],['Soccer Stadium'],['Tilted Towers'],['Dusty Divot'],['Retail Row'],['Lonely Lodge']],
    [['Snobby Shores'],['Greasy Grove'],['Shifty Shafts'],['Salty Springs'],[""],['Racing Course']],
    [['You fell in water'],['Viking Hill'],[""],['Fatal Fields'],["Paradise Palms"],[""]],
    [['You fell in water'],['You fell in water'],['Flush Factory'],['Lucky landing'],['Mexican Town'],[""]]]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fill = '#ccffff'
tex = 'Loot Lake'
x = 1
y = 2
loc = bigmap[x][y]
img = pygame.image.load('kidfort.PNG')
img.convert()
rect = img.get_rect()


async def t1():
    global bigmap,running,screen,clock,dt,fill,tex,x,y,loc,player_pos,img,rect

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(fill)

        
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
                tex = f'{loc[0]}'
                if loc[0] == 'You fell in water':
                    exit()


        elif keys[pygame.K_s]:
            player_pos.y += 600 * dt
            if player_pos.y > 720:
                if x!=5: 
                    x+=1

                loc = bigmap[x][y]
                player_pos.y = 0
                tex = f'{loc[0]}'
                if loc[0] == 'You fell in water':
                    exit()   
                

        elif keys[pygame.K_a]:
            player_pos.x -= 600 * dt
            if player_pos.x < 0:
                if y!= 0:
                    y-=1

                loc = bigmap[x][y]
                player_pos.x = 1280
                tex = f'{loc[0]}'
                if loc[0] == 'You fell in water':
                    exit()
                
        elif keys[pygame.K_d]:
            player_pos.x += 600 * dt
            
            if player_pos.x > 1280:
                if y!= 5:
                    y+=1

                loc = bigmap[x][y]
                player_pos.x = 0
                tex = f'{loc[0]}'
                if loc[0] == 'You fell in water':
                    exit()

        
        ches = pygame.image.load('chest.png')
        ches.convert()
        crect = ches.get_rect()
        crect.center = (1580 // 2, 1000 // 2)
        screen.blit(ches,crect)



                
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        
 
        
async def t2():
    await asyncio.sleep(1)
    ches = pygame.image.load('chest.png')
    ches.convert()
    crect = ches.get_rect()
    crect.center = (1580 // 2, 1000 // 2)
    screen.blit(ches,crect)
    pass

async def t3():
    global bigmap,running,screen,clock,dt,fill,tex,x,y,loc,player_pos,img,rect
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    pass
    
async def main():
        await asyncio.gather(t1(),t2(),t3())

asyncio.run(main())
    
pygame.quit()