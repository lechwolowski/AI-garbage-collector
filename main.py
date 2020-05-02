import time
import os
import pygame
import numpy as np
from numpy import genfromtxt
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from helpler import Render_Element
from GC_Env import GC_Env
from Deep_Q_Learning.GC_Env import GC_Env as dqn_gc_env
from a_star import A_Star
from keras.models import load_model

MOVES_DICT = {
    0: "up",
    1: "down",
    2: "left",
    3: "right",
    4: "pick_trash",
    5: "leave_trash"
}


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

draw_items, gc = env.reset()

# Initialize A*

__a_star__ = A_Star(draw_items, gc, env, refresh_screen)
__a_star__.houses_with_trash()

# dqn

dqn_env = dqn_gc_env()

for item in draw_items:
    display_group.add(draw_items[item])

display_group.add(gc)

render_game()

clock = pygame.time.Clock()


# know = Knowledge(draw_items, gc)
model = load_model(
    'trained_models\\lr=0.001_gamma=0.5___-35.90max_-1172.30avg_-4394.80min__2020-05-01_23-03.model')
# Game Loop
run_a = False
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
                # know.update()
                # know.show()
            if event.key == pygame.K_a:
                run_a = True
            if event.key == pygame.K_q:
                state = dqn_env.observe(gc=gc, draw_items=draw_items)
                prediction = model.predict(
                    np.array(state).reshape(-1, *state.shape))
                env.step(np.argmax(prediction))
                print(state)
                print(MOVES_DICT[np.argmax(prediction)], prediction)

            gc.render()

            refresh_screen()
    if run_a:
        houses, trashes = __a_star__.houses_with_trash()
        if len(houses) == 0 and gc.mixed == 0 and gc.paper == 0 and gc.glass == 0 and gc.plastic == 0:
            run_a = False

        else:
            route = __a_star__.get_to_dest()
            if len(route) > 0:
                x, y = route[0]
                if x - gc.col != 0:
                    if x - gc.col < 0:
                        env.step(2)
                    else:
                        env.step(3)
                elif y - gc.row != 0:
                    if y - gc.row < 0:
                        env.step(0)
                    else:
                        env.step(1)

                time.sleep(0.3)

            elif len(route) == 0:
                env.step(4)
                env.step(5)

        gc.render()

        refresh_screen()

    clock.tick(30)
