import time
import os
import pygame
import numpy as np
from sklearn import tree
from keras.models import load_model
from config import WINDOW_HEIGHT, WINDOW_WIDTH, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH, MAP
from __gc_env__ import GcEnv
from Deep_Q_Learning.__gc_env__ import GcEnv as dqn_gc_env
from a_star import AStar
from Tree.part_map import part_map
from Tree.part_map import save_to_file
from Tree.part_map import save_to_file_1
from Tree.part_map import read_table
from Tree.decision_tree import make_tree
from Tree.part_map import check_house_trash


MOVES_DICT = {
    0: "up",
    1: "down",
    2: "left",
    3: "right",
    4: "pick_trash",
    5: "leave_trash"
}

x_list = []  # lista otoczeń
y_list = []  # lista ruchów
maps = []
actions = []


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
    'trained_models', 'half_trained_unlimited.model'))

# Game Loop
RUN_A = False
RUN_A_LEARN = False
RUNNING = True
tree_loaded = False
licznik = 0
ROUTE = []
prv_move = -1
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
            if event.key == pygame.K_t:  # zbieranie danych z A* do tablic
                RUN_A_LEARN = True
            if event.key == pygame.K_o:  # odpalenie z drzewa decyzyjnego
                if not tree_loaded:
                    # GC.set_limit(100000)
                    read_table(maps, 'Xlearn.txt', 0)
                    read_table(actions, 'Ylearn.txt', 1)
                    #print("przed maketree")
                    clf = make_tree(maps, actions)
                    tree_loaded = True
                    #print("po maketree")
                state_map = []
                state_map = part_map(MAP, GC.draw_items,
                                     GC.row, GC.col, prv_move)
                print("state_map=", state_map)
                step = clf.predict([state_map])
                print("STEP=", step)
                prv_move = step[0]
                if check_house_trash(GC.col, GC.row, GC.draw_items):
                    print("akcja smieci")
                    ENV.step(4)
                    ENV.step(5)
                    GC.update()
                ENV.step(step[0])

            if event.key == pygame.K_q:
                GC.set_limit(100)
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
            if not ROUTE:
                ROUTE = __a_star__.get_to_dest()
            if len(ROUTE) > 0:
                X, Y = ROUTE.pop(0)
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

                # time.sleep(0.3)

            elif len(ROUTE) == 0:
                ENV.step(4)
                ENV.step(5)
                GC.update()
        GC.render()

        refresh_screen()

    if RUN_A_LEARN:
        # GC.set_limit(100000)
        HOUSES, _ = __a_star__.houses_with_trash()
        if len(HOUSES) == 0 and GC.mixed == 0 and GC.paper == 0 \
                and GC.glass == 0 and GC.plastic == 0:
            if licznik >= 500:
                RUN_A_LEARN = False
            else:
                licznik = licznik+1
                prv_move = -1
                print("Powtorzenie=", licznik)
                save_to_file('Xlearn.txt', x_list)
                save_to_file_1('Ylearn.txt', y_list)
                x_list = []
                y_list = []

                ENV = GcEnv()
                DRAW_ITEMS, GC = ENV.get_env()
                render_game()
                GC.render()
                refresh_screen()

                __a_star__ = AStar(DRAW_ITEMS, GC, ENV, refresh_screen)
                __a_star__.houses_with_trash()
           # read_table(maps, 'Xlearn.txt', 0)
           # read_table(actions, 'Ylearn.txt', 1)

        else:
            if not ROUTE:
                ROUTE = __a_star__.get_to_dest()
                # print(ROUTE)
           # x_list.append(part_map(MAP, GC.draw_items, GC.row, GC.col))
            if len(ROUTE) > 0:
                x_list.append(part_map(MAP, GC.draw_items,
                                       GC.row, GC.col, prv_move))
                X, Y = ROUTE.pop(0)

                if X - GC.col != 0:
                    if X - GC.col < 0:
                        prv_move = 2
                        ENV.step(2)
                        y_list.append(2)
                    else:
                        prv_move = 3
                        ENV.step(3)
                        y_list.append(3)
                elif Y - GC.row != 0:
                    if Y - GC.row < 0:
                        prv_move = 0
                        ENV.step(0)
                        y_list.append(0)
                    else:
                        prv_move = 1
                        ENV.step(1)
                        y_list.append(1)

                # time.sleep(0.1)

            elif len(ROUTE) == 0:
                ENV.step(4)
                ENV.step(5)
                # y_list.append(6)
                GC.update()
        GC.render()

        refresh_screen()
    CLOCK.tick(30)
