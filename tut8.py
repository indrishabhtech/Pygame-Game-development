import pygame
x = pygame.init()

# Initialize Game colors
red =  ()
black = (0,0,0)
white = (255,255,255)


# Creating Window
gameWindow = pygame.display.set_mode((600, 400))


screen_width = 600
screen_height = 400




# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Saap Wala Game")
pygame.display.update()

# Game Specific Variable
exit_game = False
game_over = False

# Create a Game loop to hold Game Window
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            
   
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You pressed Right Arrow Key")
    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()

quit()