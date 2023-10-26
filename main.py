import pygame
pygame.init()
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0, 0, 0))
clock = pygame.time.Clock()  # set up clock
gameover = False  # variable to run our game loop

Link = pygame.image.load('link.png')  # load your spritesheet
# this makes bright pink (255, 0, 255) transparent (sort of)
Link.set_colorkey((255, 0, 255))

# CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


# player variables
xpos = 500  # xpos of player
ypos = 200  # ypos of player
vx = 0  # x velocity of player
vy = 0  # y velocity of player
# this list holds whether each key has been pressed
keys = [False, False, False, False]
# this variable stops gravity from pulling you down more when on a platform
isOnGround = False

# animation variables variables
frameWidth = 64
frameHeight = 96
RowNum = 0  # for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


frameWidth = 64
frameHeight = 96
RowNum = 1  # for Right animation, this will need to change for other animations
frameNum = 0
ticker = 0

frameWidth = 64
frameHeight = 96
RowNum = 2  # for Up animation, this will need to change for other animations
frameNum = 0
ticker = 0


frameWidth = 64
frameHeight = 96
RowNum = 3  # for Down animation, this will need to change for other animations
frameNum = 0
ticker = 0

while not gameover:  # GAME LOOP############################################################
    clock.tick(60)  # FPS

    # Input Section------------------------------------------------------------
    for event in pygame.event.get():  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:  # keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True

            elif event.key == pygame.K_UP:
                keys[UP] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False

    # physics section--------------------------------------------------------------------
    # LEFT MOVEMENT
    if keys[LEFT] == True:
        vx = -3
        direction = LEFT
        RowNum = 0
     # RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
        direction = RIGHT
        RowNum = 1
    elif keys[DOWN] == True:
        vy = 3
        direction = DOWN
        RowNum = 2
    elif keys[UP] == True:
        vy = -6
        direction = UP
        RowNum = 3

    # turn off velocity
    else:
        vx = 0

        # JUMPING
    if keys[UP] == True and isOnGround == True:  # only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP

    # COLLISION
    if xpos > 100 and xpos < 200 and ypos+40 > 750 and ypos+40 < 770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos > 200 and xpos < 300 and ypos+40 > 650 and ypos+40 < 670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos > 300 and xpos < 400 and ypos+40 > 550 and ypos+40 < 570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos > 400 and xpos < 500 and ypos+40 > 450 and ypos+40 < 470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos > 500 and xpos < 600 and ypos+40 > 350 and ypos+40 < 370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False

    # stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760

    # gravity
    if isOnGround == False:
        vy += .2  # notice this grows over time, aka ACCELERATION

    # update player position
    xpos += vx
    ypos += vy

    # ANIMATION-------------------------------------------------------------------

    # Update Animation Information
    # Only animate when in motion
    if vx < 0:  # left animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
            # If we are over the number of frames in our sprite, reset to 0.
            # In this particular case, there are 10 frames (0 through 9)
        if frameNum > 7:
            frameNum = 0

    # Update Animation Information
    # Only animate when in motion
    if vx > 0:  # Right animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
            # If we are over the number of frames in our sprite, reset to 0.
            # In this particular case, there are 10 frames (0 through 9)
        if frameNum > 7:
            frameNum = 0

       # Update Animation Information
    # Only animate when in motion
    if vy < 0:  # DOWN animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
            # If we are over the number of frames in our sprite, reset to 0.
            # In this particular case, there are 10 frames (0 through 9)
        if frameNum > 7:
            frameNum = 0

    # Update Animation Information
    # Only animate when in motion
    if vy > 0:  # UP animation
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
            # If we are over the number of frames in our sprite, reset to 0.
            # In this particular case, there are 10 frames (0 through 9)
        if frameNum > 7:
            frameNum = 0

    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.

    screen.fill((0, 0, 0))  # wipe screen so it doesn't smear
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum,
                RowNum*frameHeight, frameWidth, frameHeight))
    # first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))

    # second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))

    # third platform
    pygame.draw.rect(screen, (51, 51, 255), (300, 550, 100, 20))

    # forth platform
    pygame.draw.rect(screen, (51, 153, 255), (400, 450, 100, 20))

    # fifth platform
    pygame.draw.rect(screen, (51, 221, 255), (500, 350, 100, 20))

    pygame.display.flip()  # this actually puts the pixel on the screen

# end game loop------------------------------------------------------------------------------
pygame.quit()
