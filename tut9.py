import pygame
x = pygame.init()

# Initialize Game colors
red =  ()
black = (0,0,0)
white = (255,255,255)


# Creating Window
screen_width = 600
screen_height = 400
gameWindow = pygame.display.set_mode((600, 400))




# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Saap Wala Game")
pygame.display.update()

# Game Specific Variable
exit_game = False
game_over = False
snake_x = 45
snake_y = 40
snake_size = 10


# Create a Game loop to hold Game Window
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            
    #Game Canvas Background 
    gameWindow.fill(white)
    
    # Create Snake ( where , color, cordinates)
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size, snake_size])
    
    # Update the functions
    pygame.display.update()

pygame.quit()

quit()