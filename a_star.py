from models.__house__ import House
from math import fabs
from models.Trash import Trash
from config import MAP_HEIGHT, MAP_WIDTH, MAP
from models.Road import Road
import numpy as np
from helpler import is_within_height, is_within_width
import heapq
import time


class A_Star:
    TRASH_TYPES = ["mixed", "paper", "glass", "plastic"]

    def __init__(self, draw_items, gc, env, refresh_screen):
        super().__init__()
        self.draw_items, self.gc, self.env, self.refresh_screen = draw_items, gc, env, refresh_screen
        self.houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

    def houses_with_trash(self):
        houses = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], House), self.draw_items))))

        trashes = list(map(lambda item: self.draw_items[item], list(filter(lambda item: isinstance(
            self.draw_items[item], Trash), self.draw_items))))
        # houses = filter(lambda house: (lambda trash_type: getattr(
        #     house, trash_type) > 5, trash_types), houses)
        # houses = filter(lambda house: getattr(house, "mixed") > 5, houses)
        filtered_houses = []
        for house in houses:
            empty = True
            for trash_type in self.TRASH_TYPES:
                if getattr(house, trash_type) > 0:
                    empty = False
            if not empty:
                filtered_houses.append(house)
        return filtered_houses, trashes
        # trash quantity/distance

    def best_move(self):
        houses, trashes = self.houses_with_trash()

        score = []
        for t_type in self.TRASH_TYPES:
            if getattr(self.gc, t_type) == self.gc.limit or len(houses) == 0:
                for trash in trashes:
                    if trash.trash_type == t_type and getattr(self.gc, t_type) != 0:
                        return (trash.col, trash.row)

        for house in houses:
            house_trash_ammount = 0
            for trash in self.TRASH_TYPES:
                house_trash_ammount += getattr(house, trash)
            distance = fabs(self.gc.col - house.col) + \
                fabs(self.gc.row - house.row)
            score.append({"score": house_trash_ammount /
                          distance, "position": (house.col, house.row)})

        return sorted(score, key=lambda i: i['score'], reverse=True)[0]["position"]

    def get_to_dest(self):
        road_pos_array = np.zeros((MAP_HEIGHT, MAP_WIDTH))

        for x, y in self.draw_items:
            if MAP[y][x] == "Road":
                road_pos_array[y, x] = 1

        start = (self.gc.col, self.gc.row)

        route = astar(array=road_pos_array, start=start,
                      goal=self.best_move())

        return route


def astar(array, start, goal):
    def heuristic(a, b):
        return fabs((b[0] - a[0])) + fabs((b[1] - a[1]))

    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()

    came_from = {}

    gscore = {start: 0}

    fscore = {start: heuristic(start, goal)}

    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current[0] == goal[0] or current[1] == goal[1]:
            if fabs(current[0] - goal[0]) == 1 or fabs(current[1] - goal[1]) == 1:
                data = []

                while current in came_from:

                    data.append(current)

                    current = came_from[current]

                data.reverse()

                return data

        close_set.add(current)

        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[1]:

                if 0 <= neighbor[1] < array.shape[0]:

                    if array[neighbor[1]][neighbor[0]] == 0:

                        continue

                else:

                    # array bound y walls

                    continue

            else:

                # array bound x walls

                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                came_from[neighbor] = current

                gscore[neighbor] = tentative_g_score

                fscore[neighbor] = tentative_g_score + \
                    heuristic(neighbor, goal)

                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False
