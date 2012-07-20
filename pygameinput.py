import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

#font
basicFont = pygame.font.SysFont(None, 38)

# set up the colors
BLACK = (0, 0, 0)
silver = (192, 192, 192)
cornflowerblue = (100, 149, 237)
white = (255, 255, 255)

# set up the player1 and food data structure
foodCounter = 0
NEWFOOD = 10
FOODSIZE = 20
player1 = pygame.Rect(300, 100, 50, 50)
player2 = pygame.Rect(100, 300, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# set up movement variables player1
moveLeft1 = False
moveRight1 = False
moveUp1 = False
moveDown1 = False
MOVESPEED = 6

#player2
moveLeft2 = False
moveRight2 = False
moveUp2 = False
moveDown2 = False
MOVESPEED = 6

count1 = 0
count2 = 0


# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #player1
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT:
                moveRight1 = False
                moveLeft1 = True
            if event.key == K_RIGHT:
                moveLeft1 = False
                moveRight1 = True
            if event.key == K_UP:
                moveDown1 = False
                moveUp1 = True
            if event.key == K_DOWN:
                moveUp1 = False
                moveDown1 = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft1 = False
            if event.key == K_RIGHT:
                moveRight1 = False
            if event.key == K_UP:
                moveUp1 = False
            if event.key == K_DOWN:
                moveDown1 = False
            if event.key == ord('/'):
                player1.top = random.randint(0, WINDOWHEIGHT - player1.height)
                player1.left = random.randint(0, WINDOWWIDTH - player1.width)

        #player2
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == ord('a'):
                moveRight2 = False
                moveLeft2 = True
            if event.key == ord('d'):
                moveLeft2 = False
                moveRight2 = True
            if event.key == ord('w'):
                moveDown2 = False
                moveUp2 = True
            if event.key == ord('s'):
                moveUp2 = False
                moveDown2 = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord('a'):
                moveLeft2 = False
            if event.key == ord('d'):
                moveRight2 = False
            if event.key == ord('w'):
                moveUp2 = False
            if event.key == ord('s'):
                moveDown2 = False
            if event.key == ord('x'):
                player2.top = random.randint(0, WINDOWHEIGHT - player2.height)
                player2.left = random.randint(0, WINDOWWIDTH - player2.width)
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    if len(foods) == 0:
        print "You win!"
        pygame.quit()
        sys.exit()

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the player1
    if moveDown1 and player1.bottom < WINDOWHEIGHT:
        player1.top += MOVESPEED
    if moveUp1 and player1.top > 0:
        player1.top -= MOVESPEED
    if moveLeft1 and player1.left > 0:
        player1.left -= MOVESPEED
    if moveRight1 and player1.right < WINDOWWIDTH:
        player1.right += MOVESPEED

    #move player2
    if moveDown2 and player2.bottom < WINDOWHEIGHT:
        player2.top += MOVESPEED
    if moveUp2 and player2.top > 0:
        player2.top -= MOVESPEED
    if moveLeft2 and player2.left > 0:
        player2.left -= MOVESPEED
    if moveRight2 and player2.right < WINDOWWIDTH:
        player2.right += MOVESPEED

    # draw the player1 and player2 onto the surface
    pygame.draw.rect(windowSurface, cornflowerblue, player1)
    pygame.draw.rect(windowSurface, white, player2)

    text = basicFont.render('Player1: %s Player2: %s' % (count1, count2), True, BLACK, cornflowerblue)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.y = windowSurface.get_rect().y

    #draw the text
    windowSurface.blit(text, textRect)

    # check if the players have intersected with any food squares.
    for food in foods[:]:
        if food != None:
            if player1.colliderect(food):
                foods.remove(food)
                count1 = count1 +1
            if player2.colliderect(food):
                count2 = count2 +1
                foods.remove(food)

    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, silver, foods[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)