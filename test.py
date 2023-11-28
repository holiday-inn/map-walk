import pygame

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
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(fill)

    pygame.draw.circle(screen, "black", player_pos, 40)
    
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(tex, True, '#ccffff', 'black')
    textRect = text.get_rect()
    textRect.center = (1280 // 2, 100 // 2)
    screen.blit(text, textRect)
    img = pygame.image.load('kidfort.PNG')
    img.convert()
    rect = img.get_rect()
    rect.center = player_pos
    screen.blit(img, rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt

        if player_pos.y < 0:
            player_pos.y = 720


    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        if player_pos.y > 720:
            player_pos.y = 0
            fill = '#cc00ff'
            tex = 'Dusty'
            

    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        if player_pos.x < 0:
            player_pos.x = 1280
            
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        if player_pos.x > 1280:
            player_pos.x = 0
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()