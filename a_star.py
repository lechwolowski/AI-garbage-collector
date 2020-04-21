from models.House import House
from math import fabs
from models.Trash import Trash


class A_Star:
    TRASH_TYPES = ["mixed", "paper", "glass", "plastic"]

    def __init__(self, draw_items, gc):
        super().__init__()
        self.draw_items, self.gc = draw_items, gc
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
            if getattr(self.gc, t_type) == self.gc.limit:
                for trash in trashes:
                    print(trash.trash_type, t_type)
                    if trash.trash_type == t_type:
                        print(trash.col, trash.row)
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
