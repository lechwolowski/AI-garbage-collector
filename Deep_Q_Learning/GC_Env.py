from Deep_Q_Learning.q_gc import Garbage_Collector
from helpler import __render_element__
from models.__house__ import House
from models.Road import Road
from config import MAP_WIDTH, MAP_HEIGHT, NUMBER_OF_HOUSES
import numpy as np
from timeit import default_timer as timer


class GC_Env:
    OBSERVATION_SPACE_VALUES = (36 + NUMBER_OF_HOUSES,)
    ACTION_SPACE_SIZE = 6

    def reset(self):
        self.draw_items = {(x, y): __render_element__(x, y)
                           for x in range(MAP_WIDTH) for y in range(MAP_HEIGHT)}
        self.gc = Garbage_Collector(self.draw_items)
        self.actions = {
            0: self.gc.move_up,
            1: self.gc.move_down,
            2: self.gc.move_left,
            3: self.gc.move_right,
            4: self.gc.pick_trash,
            5: self.gc.leave_trash
        }

        return self.observe(self.gc, self.draw_items)

    def observe(self, gc, draw_items):
        roads = list(filter(lambda item: isinstance(
            draw_items[item], Road), draw_items))

        gc_pos = roads.index((gc.col, gc.row))

        observation = np.full(self.OBSERVATION_SPACE_VALUES, -1)
        observation[gc_pos] = 1

        houses = list(map(lambda item: draw_items[item], list(filter(lambda item: isinstance(
            draw_items[item], House), draw_items))))

        houses_trash = [max([(int(getattr(house, item) != 0) - 0.5) * 2 for item in
                             ["mixed", "paper", "glass", "plastic"]]) for house in houses]

        observation[-NUMBER_OF_HOUSES:] = houses_trash

        return observation
        # gc_trash = [int(getattr(self.gc, item) == self.gc.limit)
        #             for item in ["mixed", "paper", "glass", "plastic", "limit"]]
        # new_observation = np.zeros(self.OBSERVATION_SPACE_VALUES)

        # new_observation[self.gc.col, self.gc.row] = gc_trash

    def step(self, action):
        action_result = self.actions[action]()

        new_observation = self.observe(self.gc, self.draw_items)

        if action_result is False:
            reward = -1
        elif action_result is True:
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

        # if sum(new_observation[-NUMBER_OF_HOUSES:]) < NUMBER_OF_HOUSES:
        #     done = True

        return new_observation, reward, done
