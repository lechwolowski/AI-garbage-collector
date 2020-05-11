import time
import os
import pygame
import numpy as np
from keras.models import load_model
from config import WINDOW_HEIGHT, WINDOW_WIDTH, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from __gc_env__ import GcEnv
from Deep_Q_Learning.__gc_env__ import GcEnv as dqn_gc_env
from a_star import AStar

MOVES_DICT = {
    0: "up",
    1: "down",
    2: "left",
    3: "right",
    4: "pick_trash",
    5: "leave_trash"
}


def refresh_screen():
    col, row = GC.col, GC.row
    for _ in range(4):
        for i in range(-1, 2):
            if row + i >= 0 and row + i < MAP_HEIGHT:
                WINDOW.blit(DRAW_ITEMS[col, row + i].image,
                            (col * CELL_SIZE, (row + i) * CELL_SIZE))
            if col + i >= 0 and col + i < MAP_WIDTH:
                WINDOW.blit(DRAW_ITEMS[col + i, row].image,
                            ((col + i) * CELL_SIZE, row * CELL_SIZE))
    for _ in range(4):
        WINDOW.blit(GC.image, (col * CELL_SIZE, row * CELL_SIZE))
    pygame.display.update()


def render_game():
    for _ in range(4):
        DISPLAY_GROUP.draw(WINDOW)
    pygame.display.flip()


# pylint: disable=no-member
pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

DISPLAY_GROUP = pygame.sprite.Group()

ENV = GcEnv()

DRAW_ITEMS, GC = ENV.get_env()

# Initialize A*

__a_star__ = AStar(DRAW_ITEMS, GC, ENV, refresh_screen)
__a_star__.houses_with_trash()

# dqn

DQN_ENV = dqn_gc_env()

for item in DRAW_ITEMS:
    DISPLAY_GROUP.add(DRAW_ITEMS[item])

DISPLAY_GROUP.add(GC)

render_game()

CLOCK = pygame.time.Clock()

MODEL = load_model(os.path.join(
    'trained_models', 'Limited-60k'))

# Game Loop
RUN_A = False
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ENV.step(2)
            if event.key == pygame.K_RIGHT:
                ENV.step(3)
            if event.key == pygame.K_UP:
                ENV.step(0)
            if event.key == pygame.K_DOWN:
                ENV.step(1)
            if event.key == pygame.K_SPACE:
                ENV.step(4)
                ENV.step(5)
            if event.key == pygame.K_a:
                RUN_A = True
            if event.key == pygame.K_q:
                state = DQN_ENV.observe(__gc__=GC, draw_items=DRAW_ITEMS)
                prediction = MODEL.predict(
                    np.array(state).reshape(-1, *state.shape))
                ENV.step(np.argmax(prediction))
                print(state)
                print(MOVES_DICT[np.argmax(prediction)], prediction)

            GC.render()

            refresh_screen()
    if RUN_A:
        HOUSES, _ = __a_star__.houses_with_trash()
        if len(HOUSES) == 0 and GC.mixed == 0 and GC.paper == 0 \
                and GC.glass == 0 and GC.plastic == 0:
            RUN_A = False

        else:
            ROUTE = __a_star__.get_to_dest()
            if len(ROUTE) > 0:
                X, Y = ROUTE[0]
                if X - GC.col != 0:
                    if X - GC.col < 0:
                        ENV.step(2)
                    else:
                        ENV.step(3)
                elif Y - GC.row != 0:
                    if Y - GC.row < 0:
                        ENV.step(0)
                    else:
                        ENV.step(1)

                time.sleep(0.3)

            elif len(ROUTE) == 0:
                ENV.step(4)
                ENV.step(5)
                GC.update()

        GC.render()

        refresh_screen()

    CLOCK.tick(30)
