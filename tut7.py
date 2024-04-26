import pygame
x = pygame.init()

# Creating Window
gameWindow = pygame.display.set_mode((600, 400))


pygame.display.set_caption("Saap Wala Game")



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


pygame.quit()

quit()