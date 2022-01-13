import pygame
# importing key from pygame so we can check for key presses - Used to move the player after pressing the arow keys
from pygame import key
#intializing pygame (init stands for initialize)
pygame.init()


screenHeight = 500
screenWidth = 500
playerX = 10
playerY = 10
PlayerVelocity = 5

#making the game window with a height and width value which is defined onthe top. To chnage the screen dimesions change the screenWidht or screeHeight value
screen = pygame.display.set_mode((screenHeight,screenWidth))
#setting the window name as "First Python Game"
pygame.display.set_caption("First Python Game")




#keeps the window opens due to the while loop
running = True
while running == True:
    pygame.time.delay(30)

    #checks if close button is pressed and closes the game if it is
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

    #screen clearing so old frames do not remain
    screen.fill((0,0,0))
    #drawing the player
    pygame.draw.rect(screen, (255,0,0) , (playerX , playerY , 50 , 50)) 
    #screen update
    pygame.display.update()

    
#Quit the game if game is not running       
pygame.quit()




