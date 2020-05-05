import heapq
from math import fabs
import numpy as np
from models.__house__ import House
from models.__trash__ import Trash
from config import MAP_HEIGHT, MAP_WIDTH, MAP


class AStar:
    TRASH_TYPES = ["mixed", "paper", "glass", "plastic"]

    def __init__(self, draw_items, gc, env, refresh_screen):
        super().__init__()
        self.__draw_items__, self.__gc__, self.__env__, self.__refresh_screen__ = \
            draw_items, gc, env, refresh_screen
        self.__houses__ = list(map(lambda item: self.__draw_items__[item],
                                   list(filter(lambda item: isinstance(
                                       self.__draw_items__[item], House), self.__draw_items__))))

    def houses_with_trash(self):
        houses = list(map(lambda item: self.__draw_items__[item],
                          list(filter(lambda item: isinstance(
                              self.__draw_items__[item], House), self.__draw_items__))))

        trashes = list(map(lambda item: self.__draw_items__[item],
                           list(filter(lambda item: isinstance(
                               self.__draw_items__[item], Trash), self.__draw_items__))))

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
            if getattr(self.__gc__, t_type) == self.__gc__.limit or len(houses) == 0:
                for trash in trashes:
                    if trash.trash_type == t_type and getattr(self.__gc__, t_type) != 0:
                        return (trash.col, trash.row)

        for house in houses:
            house_trash_ammount = 0
            for trash in self.TRASH_TYPES:
                house_trash_ammount += getattr(house, trash)
            distance = fabs(self.__gc__.col - house.col) + \
                fabs(self.__gc__.row - house.row)
            score.append({"score": house_trash_ammount / distance,
                          "position": (house.col, house.row)})

        return sorted(score, key=lambda i: i['score'], reverse=True)[0]["position"]

    def get_to_dest(self):
        road_pos_array = np.zeros((MAP_HEIGHT, MAP_WIDTH))

        for __x__, __y__ in self.__draw_items__:
            if MAP[__y__][__x__] == "Road":
                road_pos_array[__y__, __x__] = 1

        start = (self.__gc__.col, self.__gc__.row)

        route = astar(array=road_pos_array, start=start,
                      goal=self.best_move())

        return route


def astar(array, start, goal):
    def heuristic(__a__, __b__):
        return fabs((__b__[0] - __a__[0])) + fabs((__b__[1] - __a__[1]))

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
