from models.Garbage_Collector import Garbage_Collector
from helpler import Render_Element
from models.House import House
from config import MAP_WIDTH, MAP_HEIGHT
import numpy as np


class GC_Env:
    OBSERVATION_SPACE_VALUES = (2 + 1 * 4 + 6 * 4,)
    ACTION_SPACE_SIZE = 6

    def __init__(self):
        self.reset()
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
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))
        observation = [
            self.gc.col/(MAP_WIDTH - 1),
            self.gc.row / (MAP_HEIGHT - 1),
            self.gc.mixed / self.gc.limit, self.gc.paper / self.gc.limit,
            self.gc.glass / self.gc.limit, self.gc.plastic / self.gc.limit,
        ]
        for house in houses:
            for item in ["mixed", "paper", "glass", "plastic"]:
                observation.append(getattr(house, item) / house.limit)

        return observation

    def step(self, action):
        action_result = self.actions[action]()
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

        new_observation = [
            self.gc.col/(MAP_WIDTH - 1),
            self.gc.row / (MAP_HEIGHT - 1),
            self.gc.mixed / self.gc.limit, self.gc.paper / self.gc.limit,
            self.gc.glass / self.gc.limit, self.gc.plastic / self.gc.limit,
        ]
        for house in houses:
            for item in ["mixed", "paper", "glass", "plastic"]:
                new_observation.append(getattr(house, item) / house.limit)

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
