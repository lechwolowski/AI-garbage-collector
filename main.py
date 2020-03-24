import pygame
from models.Grass import Grass
from config import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()

display_group = pygame.sprite.Group()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

draw_items = [[Grass(x, y) for x in range(16)] for y in range(10)]

# todo layers to display inside display loop

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
            if event.key == pygame.K_RIGHT:
                print("Right")
            if event.key == pygame.K_UP:
                print("Up")
            if event.key == pygame.K_DOWN:
                print("Down")

        for line in draw_items:
            for item in line:
                display_group.add(item)

        # display_group.update()
        # draw sprite group - everything that was added to display_group
        display_group.draw(WINDOW)

        pygame.display.flip()
