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
velocity_x =1
velocity_y = 1
snake_size = 10
fps = 30

clock = pygame.time.Clock()

# Create a Game loop to hold Game Window
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x+1
            if event.key == pygame.K_LEFT:
                snake_x = snake_x-1
            if event.key == pygame.K_UP:
                snake_y = snake_y-1
            if event.key == pygame.K_DOWN:
                snake_y = snake_y+1
                
    #Updae snake position according to velocity
    snake_x = snake_x +velocity_x
    snake_y = snake_y +velocity_y
            
    #Game Canvas Background 
    gameWindow.fill(white)
    
    # Create Snake ( where , color, cordinates)
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size, snake_size])
    
    # Update the functions
    pygame.display.update()
    
    clock.tick(fps)

pygame.quit()

quit()