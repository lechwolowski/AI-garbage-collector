import pygame
from models.Grass import Grass
from models.Garbage_Collector import Garbage_Collector
from models.Road import Road
from models.House import House
from models.Pond import Pond
from models.Tree import Tree
from models.Factory import Factory
from models.Dump import Dump
from config import WINDOW_HEIGHT, WINDOW_WIDTH


pygame.init()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

display_group = pygame.sprite.Group()

draw_items = [[Grass(x, y) for x in range(16)] for y in range(10)]

for line in draw_items:
    for item in line:
        display_group.add(item)

gc = Garbage_Collector()

display_group.add(gc)

clock = pygame.time.Clock()

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

    display_group.draw(WINDOW)

    pygame.display.flip()

    clock.tick(30)
