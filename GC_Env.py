from models.Garbage_Collector import Garbage_Collector
from helpler import Render_Element
from models.House import House
from config import MAP_WIDTH, MAP_HEIGHT
import numpy as np


class GC_Env:
    OBSERVATION_SPACE_VALUES = (2 + 1 * 4 + 6 * 4,)
    ACTION_SPACE_SIZE = 6

    def reset(self):
        self.draw_items = {(x, y): Render_Element(x, y)
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

        return self.draw_items, self.gc

    def step(self, action):
        self.actions[action]()
