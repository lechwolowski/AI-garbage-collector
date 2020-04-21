import time
import os
import pygame
from numpy import genfromtxt
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from helpler import Render_Element
from GC_Env import GC_Env
from a_star import A_Star


def refresh_screen():
    col, row = gc.col, gc.row
    for _ in range(4):
        for i in range(-1, 2):
            if row + i >= 0 and row + i < MAP_HEIGHT:
                WINDOW.blit(draw_items[col, row + i].image,
                            (col * CELL_SIZE, (row + i) * CELL_SIZE))
            if col + i >= 0 and col + i < MAP_WIDTH:
                WINDOW.blit(draw_items[col + i, row].image,
                            ((col + i) * CELL_SIZE, row * CELL_SIZE))
    for _ in range(4):
        WINDOW.blit(gc.image, (col * CELL_SIZE, row * CELL_SIZE))
    pygame.display.update()


def render_game():
    for _ in range(4):
        display_group.draw(WINDOW)
    pygame.display.flip()


pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

display_group = pygame.sprite.Group()

env = GC_Env()

_, draw_items, gc = env.reset()

# Initialize A*

__a_star__ = A_Star(draw_items, gc)
__a_star__.houses_with_trash()

for item in draw_items:
    display_group.add(draw_items[item])

display_group.add(gc)

render_game()

clock = pygame.time.Clock()


# know = Knowledge(draw_items, gc)

# Game Loop
run_ql = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                env.step(2)
            if event.key == pygame.K_RIGHT:
                env.step(3)
            if event.key == pygame.K_UP:
                env.step(0)
            if event.key == pygame.K_DOWN:
                env.step(1)
            if event.key == pygame.K_SPACE:
                env.step(4)
                env.step(5)
                __a_star__.houses_with_trash()
                # know.update()
                # know.show()
            gc.render()

            refresh_screen()

    clock.tick(30)
