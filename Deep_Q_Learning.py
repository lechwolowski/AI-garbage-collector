from os.path import isfile
import numpy as np
from time import time
from models.House import House
from random import randint
from helpler import Render_Element
from models.Garbage_Collector import Garbage_Collector
from config import MAP_WIDTH, MAP_HEIGHT
from models.Road import Road

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


class Deep_Q_Learning:
    def __init__(self, gc=None, draw_items=None, q_table=None):
        self.q_table = q_table
        self.gc = gc
        self.draw_items = draw_items
        self.actions = {
            0: self.gc.move_up,
            1: self.gc.move_down,
            2: self.gc.move_left,
            3: self.gc.move_right,
            4: self.gc.pick_trash,
            5: self.gc.leave_trash
        }
        self.runs = 0

    def reset(self):
        self.draw_items = {(x, y): Render_Element(x, y)
                           for x in range(MAP_WIDTH) for y in range(MAP_HEIGHT)}
        self.gc = Garbage_Collector(self.draw_items)

    def step(self, action):
        action_result = self.actions[action]()
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

        new_observation = {"gc-pos": (self.gc.col/(MAP_WIDTH - 1),
                                      self.gc.row / (MAP_HEIGHT - 1)),
                           "gc-trash": (self.gc.mixed / self.gc.limit, self.gc.paper / self.gc.limit,
                                        self.gc.glass / self.gc.limit, self.gc.plastic / self.gc.limit),
                           "houses": ((house.mixed / house.limit, house.paper / house.limit, house.glass / house.limit, house.plastic / house.limit) for house in houses)
                           }

        if action_result == False:
            reward = -10
        elif action_result == True:
            reward = -0.1
        else:
            reward = action_result

        done = True
        if not self.gc.is_empty():
            done = False
        else:
            for item in self.draw_items:
                if isinstance(self.draw_items[item], House) and not self.draw_items[item].is_empty():
                    done = False
                    break

        return new_observation, reward, done

    def run(self):
        # self.set_raw_game()
        self.houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

        input_shape = (2 * 4 * len(self.houses) * 4,)
        model = Sequential([
            Dense(units=512, activation="sigmoid", input_shape=input_shape),
            Dense(512, activation='sigmoid'),
            Dense(units=6, activation='softmax')
        ])
        print(model.summary())

        policy = EpsGreedyQPolicy()
        memory = SequentialMemory(limit=50000, window_length=1)
        dqn = DQNAgent(model=model, nb_actions=len(self.actions), memory=memory, nb_steps_warmup=10,
                       target_model_update=1e-2, policy=policy)
        dqn.compile(Adam(lr=1e-3), metrics=['mae'])


dql = Deep_Q_Learning()
dql.run()
