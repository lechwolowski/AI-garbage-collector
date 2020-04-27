from Deep_Q_Learning.q_gc import Garbage_Collector
from helpler import Render_Element
from models.House import House
from config import MAP_WIDTH, MAP_HEIGHT
import numpy as np
from timeit import default_timer as timer


class GC_Env:
    OBSERVATION_SPACE_VALUES = (MAP_WIDTH + MAP_HEIGHT + 2 * 4 + 6 * 4,)
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
        self.prev_10_moves = np.full(10,-1)
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))
        observation = np.zeros((MAP_WIDTH + MAP_HEIGHT,))
        observation[self.gc.col] = 1
        observation[MAP_WIDTH + self.gc.row] = 1
        observation = np.append(observation, int(self.gc.mixed == self.gc.limit))
        observation = np.append(observation, int(self.gc.paper == self.gc.limit))
        observation = np.append(observation, int(self.gc.glass == self.gc.limit))
        observation = np.append(observation, int(self.gc.plastic == self.gc.limit))
        observation = np.append(observation, int(self.gc.mixed == 0))
        observation = np.append(observation, int(self.gc.paper == 0))
        observation = np.append(observation, int(self.gc.glass == 0))
        observation = np.append(observation, int(self.gc.plastic == 0))
        for house in houses:
            for item in ["mixed", "paper", "glass", "plastic"]:
                observation = np.append(observation, getattr(house, item) == house.limit)

        return observation

    def step(self, action):
        self.prev_10_moves = np.delete(np.append(self.prev_10_moves, action), 0)
        
        action_result = self.actions[action]()
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

        new_observation = np.zeros((MAP_WIDTH + MAP_HEIGHT,))
        new_observation[self.gc.col] = 1
        new_observation[MAP_WIDTH + self.gc.row] = 1
        new_observation = np.append(new_observation, int(self.gc.mixed == self.gc.limit))
        new_observation = np.append(new_observation, int(self.gc.paper == self.gc.limit))
        new_observation = np.append(new_observation, int(self.gc.glass == self.gc.limit))
        new_observation = np.append(new_observation, int(self.gc.plastic == self.gc.limit))
        new_observation = np.append(new_observation, int(self.gc.mixed == 0))
        new_observation = np.append(new_observation, int(self.gc.paper == 0))
        new_observation = np.append(new_observation, int(self.gc.glass == 0))
        new_observation = np.append(new_observation, int(self.gc.plastic == 0))
        for house in houses:
            for item in ["mixed", "paper", "glass", "plastic"]:
                new_observation = np.append(new_observation, int(getattr(house, item) == 0))

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

        inf_loop = True
        for move in self.prev_10_moves:
            if move > 3 and inf_loop == True:
                inf_loop = False
        
        if inf_loop:
            it = iter(self.prev_10_moves)
            even,odd = [],[]
            for ev in it:
                even.append(ev)
                odd.append(next(it))
            if len(set(even)) <= 1 and len(set(odd)) <= 1:
                # ln = len(self.prev_10_moves)
                reward = -1000

        return new_observation, reward, done
