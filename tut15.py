import pygame
import random
x = pygame.init()

# Initialize Game colors
red =  (255,0,0)
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
velocity_x =0
velocity_y = 0
# Generate food randomly for dnake on canvas
food_x = random.randint(20, screen_width/2)
food_y = random.randint(20, screen_height)/2

score = 0
init_velocity = 2
snake_size = 10
fps = 60


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# Create a Game loop to hold Game Window
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 velocity_x= init_velocity
                 velocity_y =0
            if event.key == pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y= -init_velocity
                velocity_x =0
                
            if event.key == pygame.K_DOWN:
                 velocity_x=0
                 velocity_y = init_velocity
    #Updae snake position according to velocity
    snake_x = snake_x +velocity_x
    snake_y = snake_y +velocity_y
    
    if abs(snake_x-food_x)<6 and abs(snake_y- food_y) <6:
        score  +=1
        # Generate food randomly for dnake on canvas
        food_x = random.randint(20, screen_width/2)
        food_y = random.randint(20, screen_height)/2
    
                
    #Game Canvas Background
    gameWindow.fill(white)
    
    # Update game score dynamically on the user screen
    text_screen("Score :" +str(score*10), red, 5,5)
    
    
    # Plot the Snake Food
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size]) 
    
    # Create Snake ( where , color, cordinates)
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size, snake_size])
    
    # Update the functions
    pygame.display.update()
    
    clock.tick(fps)

pygame.quit()

quit()