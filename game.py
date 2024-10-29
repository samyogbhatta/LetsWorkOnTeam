import pygame

# Initialize pygame
x = pygame.init()

# Create game window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Eat Bamboo Eat")

# Game-specific variables
exit_game = False
game_over = False

# Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed the right arrow key")

pygame.quit()
quit()
