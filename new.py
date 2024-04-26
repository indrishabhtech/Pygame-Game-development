import pygame
# x = pygame.init()
pygame.init()

# Creating Game window/Display
screen = pygame.display.set_mode((800,500))

# Set the Game title from here
pygame.display.set_caption("My Game")



# Game Specific Valriables
exit_game = False
game_over = False

# Creating a game loop

while not exit_game:
    # pass
    for event in pygame.event.get():
        # print(event )
        
        if event.type == pygame.QUIT:
            exit_game = True
            
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
                print("You pressed right aeeow key")
                
                
pygame.quit()

quit()