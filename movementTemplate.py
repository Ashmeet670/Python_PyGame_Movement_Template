import pygame
from pygame import key
pygame.init()

screenHeight = 500
screenWidth = 500
playerX = 10
playerY = 10



screen = pygame.display.set_mode((screenHeight,screenWidth))
pygame.display.set_caption("First Python Game")




#keeps the window opens due to the while loop
running = True
while running == True:
    pygame.time.delay(30)

    #checks if close button is pressed and closes th egame if it is
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # getting if keys are pressed
    keyPressed = pygame.key.get_pressed()

    #movement
    if keyPressed[pygame.K_UP] and playerY > 0:
        playerY -= PlayerVelocity
    if keyPressed[pygame.K_DOWN] and playerY < screenHeight - 50:
        playerY += PlayerVelocity
    if keyPressed[pygame.K_LEFT] and playerX > 0:
        playerX -= PlayerVelocity
    if keyPressed[pygame.K_RIGHT] and playerX < screenWidth - 50:
        playerX += PlayerVelocity
    
    if BulletShoot==False and keyPressed[pygame.K_SPACE]:
        BulletShoot = True

    #screen clearing so old frames do not remain
    screen.fill((0,0,0))
    #drawing the player
    pygame.draw.rect(screen, (255,0,0) , (playerX , playerY , 50 , 50)) 
    #screen update
    pygame.display.update()

    
#Quit the game if game is not running       
pygame.quit()




