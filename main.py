import pygame
import csv
import os
import time
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH, TRASH_GLASS_IMAGE, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from helpler import Render_Element
from Knowledge import Knowledge
from models.Trash import Trash
from q_learning import Q_Learning
from numpy import genfromtxt


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

draw_items = {(x, y): Render_Element(x, y)
              for x in range(MAP_WIDTH) for y in range(MAP_HEIGHT)}

for item in draw_items:
    display_group.add(draw_items[item])

gc = Garbage_Collector()

display_group.add(gc)

render_game()

clock = pygame.time.Clock()


# know = Knowledge(draw_items, gc)

# refresh_screen()
q_table = genfromtxt(
    f"runs/{sorted(os.listdir('runs'), reverse=True)[0]}", delimiter=',')
ql = Q_Learning(gc, draw_items, q_table)

# Game Loop
run_ql = False
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
            if event.key == pygame.K_SPACE:
                gc.pick_trash(draw_items)
                gc.leave_trash(draw_items)
                # print(ml.trash_flow())
                # know.update()
                # know.show()
                # print(ml.is_done())
                # print(draw_items[(0, 2)].mixed)
            if event.key == pygame.K_p:
                run_ql = True
                # print(ql.houses_state())
            gc.render()

            refresh_screen()
    if run_ql:
        run_ql = not ql.play()
        time.sleep(0.3)
        gc.render()
        refresh_screen()

    clock.tick(30)
