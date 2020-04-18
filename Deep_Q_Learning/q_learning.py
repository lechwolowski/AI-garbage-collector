# import tensorflow as tf
# print(tf.version)
from os.path import isfile
import numpy as np
from time import time
from models.House import House
from random import randint
from helpler import Render_Element
from models.Garbage_Collector import Garbage_Collector
from config import MAP_WIDTH, MAP_HEIGHT
from models.Road import Road
from multiprocessing import Process, Queue, Lock, Array
from shared_ndarray import SharedNDArray


class Q_Learning:
    def __init__(self, gc=None, draw_items=None, q_table=None):
        self.q_table = q_table
        self.gc = gc
        self.draw_items = draw_items
        self.actions = {
            0: self.move_up,
            1: self.move_down,
            2: self.move_left,
            3: self.move_right,
            4: self.pick_trash,
            5: self.leave_trash
        }
        self.runs = 0

    # Actions and Rewards

    def pick_trash(self):
        transfered = self.gc.pick_trash(self.draw_items)
        if transfered == 0:
            return -0.1
        else:
            return transfered * 10

    def leave_trash(self):
        transfered = self.gc.leave_trash(self.draw_items)
        if transfered == 0:
            return -0.1
        else:
            return transfered * 100

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
            return - 100

    # Table

    def is_full(self, trash_type):
        if getattr(self.gc, trash_type) == self.gc.limit:
            return True
        else:
            return False

    def is_empty(self, trash_type):
        if getattr(self.gc, trash_type) == 0:
            return True
        else:
            return False

    def is_done(self):
        if not self.gc.is_empty():
            return False
        for item in self.draw_items:
            if isinstance(self.draw_items[item], House) and not self.draw_items[item].is_empty():
                return False
        return True

    def houses_state(self):
        self.houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))
        i = 0
        summ = 0
        for house in self.houses:
            if house.is_empty():
                summ += 2 ** i
            i += 1

        return summ

    def gc_position(self):
        roads = self.extract_roads()
        return roads.index((self.gc.col, self.gc.row))

    def extract_roads(self):
        return list(filter(lambda item: isinstance(
            self.draw_items[item], Road), self.draw_items))

    def set_state(self):
        state = (self.gc_position() * 0x100 +
                 (8 * self.is_full("mixed") + 4 * self.is_full("paper") +
                  2 * self.is_full("glass") + self.is_full("plastic")) * 0x10 +
                 8 * self.is_empty("mixed") + 4 * self.is_empty("paper") +
                 2 * self.is_empty("glass") + self.is_empty("plastic")) * (2 ** 6) + \
            self.houses_state()
        return state

    # Generate new game

    def set_raw_game(self):
        self.draw_items = {(x, y): Render_Element(x, y)
                           for x in range(MAP_WIDTH) for y in range(MAP_HEIGHT)}
        self.gc = Garbage_Collector({"row": 1, "col": 1})

    def one_game_loop(self, queue, lock, q_table, alpha, gamma, epsilon):
        done = False
        i = 0
        reward_sum = 0
        while not done and i < 10000:
            state = self.set_state()
            if np.random.uniform(0, 1) < epsilon:
                action = randint(0, len(self.actions) - 1)
            else:
                lock.acquire()
                action = np.argmax(q_table.array[state])
                lock.release()
            reward = self.actions[action]()
            reward_sum += reward
            next_state = self.set_state()
            lock.acquire()
            old_value = q_table.array[state, action]
            next_max = np.max(q_table.array[next_state])
            lock.release()
            i += 1
            new_value = (1 - alpha) * old_value + alpha * \
                (reward + gamma * next_max)
            lock.acquire()
            q_table.array[state, action] = new_value
            lock.release()
            if self.is_done():
                done = True
        queue.put(i)

    def run(self, epochs=100, alpha=0.8, gamma=0.8, epsilon=0.8, epsilon_step=0.001):
        self.set_raw_game()
        print_interval = 1000
        if self.q_table is None:
            # self.q_table = np.zeros(
            #     (len(self.extract_roads()) * 2**4 * 2**4 * 2**6 * 4, 6))
            self.q_table = SharedNDArray(
                (len(self.extract_roads()) * 2**4 * 2**4 * 2**6 * 4, 6))
        moves = 0
        # reward_sum = 0
        # avg_sums = 0
        tg0 = time()
        t0 = time()
        lock = Lock()
        while self.runs < epochs:
            q = Queue()
            p = [Process(target=self.one_game_loop,
                         args=(q, lock, self.q_table, 0.8, 0.8, 0.8)) for _ in range(8)]
            for item in p:
                item.start()

            for _ in p:
                i = q.get()
                moves += i
                # sums += game_reward

                # print(0)
                # moves += i
                # sums += reward_sum
                # avg_sums += reward_sum / i
                # i, reward_sum = q.get()
                # print(1)
                # moves += i
                # sums += reward_sum
                # avg_sums += reward_sum / i
                # i, reward_sum = q.get()
                # print(2)
                # moves += i
                # sums += reward_sum
                # avg_sums += reward_sum / i
                # i, reward_sum = q.get()
                # print(3)
            for pr in p:
                pr.join()
                self.runs += 1
                epsilon -= epsilon_step

            # moves += i
            # sums += reward_sum
            # avg_sums += reward_sum / i
            if self.runs % print_interval == 0 or self.runs == 0:
                t1 = time()
                print("runs:", self.runs, "epsilon:", round(
                    epsilon, 2), "avg_moves:", moves / print_interval, "time:", round((t1 - t0), 2))
                # , "avg_moves:", moves / 40, "sum:",
                #       int(sums / 40), "average:", round(avg_sums / 40, 2), "epsilon:", round(epsilon, 2), "time:", round((t1 - t0), 2))
                moves = 0
                t0 = time()
            self.set_raw_game()
        tg1 = time()
        print("time of learning:", int((tg1 - tg0) / 60))
        saved = False
        num = 7
        while not saved and num < 1000:
            if not isfile(f"runs/run_{str(num).zfill(3)}.csv"):
                np.savetxt(f"runs/run_{str(num).zfill(3)}.csv",
                           self.q_table.array, delimiter=",")
                saved = True
            else:
                num += 1

    def test(self):
        self.set_raw_game()
        i = 0
        reward_sum = 0
        while not self.is_done() and i < 100000:
            state = self.set_state()
            action = np.argmax(self.q_table[state])
            reward = self.actions[action]()
            reward_sum += reward
            i += 1

        print("moves:", i, "sum:", int(reward_sum), "average:",
              round(reward_sum / i, 2))

    def play(self):
        state = self.set_state()
        action = np.argmax(self.q_table[state])
        reward = self.actions[action]()
        print(state, action, reward, np.argmax(
            self.q_table[state]), self.q_table[state])
        return self.is_done()
