# import tensorflow as tf
# print(tf.version)
from os.path import isfile
import numpy as np
from models.House import House
from random import randint
from helpler import Render_Element
from models.Garbage_Collector import Garbage_Collector


class Q_Learning:
    def __init__(self):
        super().__init__()
        self.q_table = np.zeros((16 * 10 * 2 * 2 * 2 * 2, 6))
        self.actions = {
            0: self.move_up,
            1: self.move_down,
            2: self.move_left,
            3: self.move_right,
            4: self.pick_trash,
            5: self.leave_trash
        }
        self.set_raw_game()

    def is_mixed_full(self):
        if self.gc.mixed == self.gc.limit:
            return True
        else:
            return False

    def is_paper_full(self):
        if self.gc.paper == self.gc.limit:
            return True
        else:
            return False

    def is_glass_full(self):
        if self.gc.glass == self.gc.limit:
            return True
        else:
            return False

    def is_plastic_full(self):
        if self.gc.plastic == self.gc.limit:
            return True
        else:
            return False

    def col(self): return self.gc.col
    def row(self): return self.gc.row

    def is_done(self):
        if not self.gc.is_empty():
            return False
        for item in self.draw_items:
            if isinstance(self.draw_items[item], House) and not self.draw_items[item].is_empty():
                return False
        return True

    def pick_trash(self):
        return self.gc.pick_trash(self.draw_items) - 2

    def leave_trash(self):
        transfered = self.gc.leave_trash(self.draw_items)
        if transfered == 0:
            return - 10
        else:
            return transfered * 10

    def move_up(self):
        if self.gc.move_up():
            return -0.01
        else:
            return -100

    def move_down(self):
        if self.gc.move_down():
            return -0.01
        else:
            return -100

    def move_left(self):
        if self.gc.move_left():
            return -0.01
        else:
            return -100

    def move_right(self):
        if self.gc.move_right():
            return -0.01
        else:
            return -100

    def set_state(self):
        state = self.row() * 0x100 + \
            self.col() * 0x10 + \
            8 * self.is_mixed_full() + 4 * self.is_paper_full() + \
            2 * self.is_glass_full() + self.is_plastic_full()
        return state

    def set_raw_game(self):
        self.draw_items = {(x, y): Render_Element(x, y)
                           for x in range(16) for y in range(10)}
        self.gc = Garbage_Collector()

    def run(self):
        epsilon = 0.8
        alpha = 0.8  # learning rate
        gamma = 0.9
        for run in range(1000):
            done = False
            i = 0
            reward_sum = 0
            while not done and i < 100000:
                state = self.set_state()
                if np.random.uniform(0, 1) < epsilon:
                    action = randint(0, len(self.actions) - 1)
                else:
                    action = np.argmax(self.q_table[state])
                reward = self.actions[action]()
                reward_sum += reward
                next_state = self.set_state()

                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])

                i += 1
                new_value = (1 - alpha) * old_value + alpha * \
                    (reward + gamma * next_max)
                self.q_table[state, action] = new_value
                if self.is_done():
                    done = True
                    epsilon -= 0.001

            print("run:", run, "moves:", i, "sum:",
                  int(reward_sum), "average:", round(reward_sum / i, 2), "epsilon:", round(epsilon, 2))
            self.set_raw_game()
        saved = False
        num = 7
        while not saved and num < 1000:
            if not isfile(f"runs/run_{str(num).zfill(3)}.csv"):
                np.savetxt(f"runs/run_{str(num).zfill(3)}.csv",
                           self.q_table, delimiter=",")
                saved = True
            else:
                num += 1
        # self.gc.render()
        # self.render_game()

    def test(self):
        done = False
        i = 0
        reward_sum = 0
        while not done and i < 100000:
            state = self.set_state()
            action = np.argmax(self.q_table[state])
            reward = self.actions[action]()
            reward_sum += reward
            i += 1
        print("moves:", i, "sum:", int(reward_sum), "average:",
              round(reward_sum / i, 2))


ql = Q_Learning()
ql.run()
ql.test()
