import pygame
from models.Grass import Grass
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()

display_group = pygame.sprite.Group()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

draw_items = [[Grass(x, y) for x in range(16)] for y in range(10)]

gc = Garbage_Collector()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gc.move_left()
            if event.key == pygame.K_RIGHT:
                gc.move_right()
            if event.key == pygame.K_UP:
                gc.move_up()
            if event.key == pygame.K_DOWN:
                gc.move_down()

        for line in draw_items:
            for item in line:
                display_group.add(item)

        display_group.add(gc)

        # display_group.update()
        # draw sprite group - everything that was added to display_group
        display_group.draw(WINDOW)

        pygame.display.flip()
