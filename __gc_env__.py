from models.__garbage_collector__ import GarbageCollector
from helpler import __render_element__
from config import MAP_WIDTH, MAP_HEIGHT


class GcEnv:

    def __init__(self):
        self.draw_items = {(x, y): __render_element__(x, y)
                           for x in range(MAP_WIDTH) for y in range(MAP_HEIGHT)}
        self.__gc__ = GarbageCollector(self.draw_items)
        self.actions = {
            0: self.__gc__.move_up,
            1: self.__gc__.move_down,
            2: self.__gc__.move_left,
            3: self.__gc__.move_right,
            4: self.__gc__.pick_trash,
            5: self.__gc__.leave_trash
        }

    def get_env(self):
        return self.draw_items, self.__gc__

    def step(self, action):
        self.actions[action]()
