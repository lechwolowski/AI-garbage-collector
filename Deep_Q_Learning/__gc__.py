from random import randint
from config import MAP_HEIGHT, MAP_WIDTH, MAP, TRASH_TYPES
from models.__house__ import House
from models.__numbers__ import Numbers
from models.__trash__ import Trash


class GarbageCollector(Numbers):
    def __init__(self, draw_items):
        self.road_positions = {row_index: {
            col_index: (True if MAP[row_index][col_index] == "Road" else False)
            for col_index in MAP[row_index]} for row_index in MAP}

        gc_initial_position = self.random_starting_position()
        self.col = gc_initial_position["col"]
        self.row = gc_initial_position["row"]

        self.mixed = 0
        self.paper = 0
        self.glass = 0
        self.plastic = 0
        self.limit = 10
        self.draw_items = draw_items

        Numbers.__init__(self, self.col, self.row)

    def random_starting_position(self):
        gc_initial_position = {"row": randint(
            0, MAP_HEIGHT - 1), "col": randint(0, MAP_WIDTH - 1)}
        while not self.road_positions[gc_initial_position["row"]][gc_initial_position["col"]]:
            gc_initial_position = {"row": randint(
                0, MAP_HEIGHT - 1), "col": randint(0, MAP_WIDTH - 1)}
        return gc_initial_position

    def is_empty(self):
        if self.mixed == 0 and self.glass == 0 and self.paper == 0 and self.plastic == 0:
            return True
        else:
            return False

    def move_up(self):
        if self.row > 0 and self.road_positions[self.row - 1][self.col]:
            self.row -= 1
            return True
        return False

    def move_down(self):
        if self.row < MAP_HEIGHT - 1 and self.road_positions[self.row + 1][self.col]:
            self.row += 1
            return True
        return False

    def move_left(self):
        if self.col > 0 and self.road_positions[self.row][self.col - 1]:
            self.col -= 1
            return True
        return False

    def move_right(self):
        if self.col < MAP_WIDTH - 1 and self.road_positions[self.row][self.col + 1]:
            self.col += 1
            return True
        return False

    def pick_trash(self):
        if self.mixed == self.limit and self.glass == self.limit and \
                self.paper == self.limit and self.plastic == self.limit:
            return -1

        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        houses_around = False
        transfered = False
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and \
                    field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, House):
                    houses_around = True

                    # debug - unit test
                    for trash_type in TRASH_TYPES:
                        gc_trash, house_trash = getattr(
                            self, trash_type), getattr(item, trash_type)
                        if house_trash and gc_trash < self.limit:
                            if gc_trash + house_trash > self.limit:
                                house_trash = self.limit - gc_trash
                            item.get_trash(trash_type=trash_type,
                                           queried_ammount=house_trash)
                            setattr(self, trash_type, getattr(self, trash_type) + house_trash)
                            transfered = True

        if houses_around and transfered:
            return 1
        return -1

    def leave_trash(self):
        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        transfered = 0
        trashes_around = False
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and \
                    field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, Trash):
                    trashes_around = True
                    if item.trash_type in TRASH_TYPES:
                        trash_ammount = getattr(self, item.trash_type)
                        if trash_ammount:
                            item.put_trash(trash_ammount)
                            setattr(self, item.trash_type, 0)
                            transfered += trash_ammount
                            break

        if trashes_around and transfered:
            return 1
        return -1
