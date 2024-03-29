import numpy as np
from Deep_Q_Learning.__gc__ import GarbageCollector
from helpler import __render_element__
from models.__house__ import House
from models.__road__ import Road
from config import MAP_WIDTH, MAP_HEIGHT, NUMBER_OF_HOUSES, TRASH_TYPES


class GcEnv:
    TRASH_INFO_LEN = 2 * len(TRASH_TYPES) + NUMBER_OF_HOUSES * len(TRASH_TYPES)
    GC_TRASH_LEN = 2 * len(TRASH_TYPES)
    OBSERVATION_SPACE_VALUES = (
        36 + TRASH_INFO_LEN,)
    ACTION_SPACE_SIZE = 6

    def __init__(self):
        self.draw_items = None
        self.__gc__ = None
        self.actions = None

    def reset(self):
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

        return self.observe(self.__gc__, self.draw_items)

    def observe(self, __gc__, draw_items):
        roads = list(filter(lambda item: isinstance(
            draw_items[item], Road), draw_items))

        gc_pos = roads.index((__gc__.col, __gc__.row))

        observation = np.full(self.OBSERVATION_SPACE_VALUES, -1)
        observation[gc_pos] = 1

        houses = list(map(lambda item: draw_items[item], list(filter(lambda item: isinstance(
            draw_items[item], House), draw_items))))

        houses_trash = [(int(getattr(house, item) != 0) - 0.5)
                        * 2 for item in TRASH_TYPES for house in houses]

        gc_trash = [(int(getattr(__gc__, item) != 0) - 0.5) * 2 for item in TRASH_TYPES] + \
            [(int(getattr(__gc__, item) != __gc__.limit) - 0.5)
             * 2 for item in TRASH_TYPES]

        observation[-self.TRASH_INFO_LEN: -self.GC_TRASH_LEN] = houses_trash
        observation[-self.GC_TRASH_LEN:] = gc_trash

        return observation

    def is_done(self, __gc__, draw_items):
        done = True
        if not __gc__.is_empty():
            done = False
        else:
            for item in draw_items:
                if isinstance(draw_items[item], House) and not draw_items[item].is_empty():
                    done = False
                    break
        return done

    def step(self, action):
        action_result = self.actions[action]()

        new_observation = self.observe(self.__gc__, self.draw_items)

        if action_result is False:
            reward = -1
        elif action_result is True:
            reward = -0.1
        else:
            reward = action_result

        done = True
        if not self.__gc__.is_empty():
            done = False
        else:
            for item in self.draw_items:
                if isinstance(self.draw_items[item], House) and not self.draw_items[item].is_empty():
                    done = False
                    break

        # if sum(new_observation[-NUMBER_OF_HOUSES:]) < NUMBER_OF_HOUSES:
        #     done = True

        return new_observation, reward, done
