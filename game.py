import pygame

# Initialize pygame
x = pygame.init()

# Create game window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Eat Bamboo0s Eat")

# Game-specific variables
exit_game = False
game_over = False

# Game loopss
while not exit_game:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You havee pressed thee right arrow key")
                print("You havee pressed thee right arrow key")

pygame.quit()
quit()
