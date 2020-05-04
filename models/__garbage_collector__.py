from random import randint
import pygame
from config import CELL_SIZE, MAP_HEIGHT, MAP_WIDTH, MAP, \
    BLACK, BLUE, GREEN, YELLOW, GARBAGE_COLLECTOR_IMAGE, TRASH_TYPES
from models.__house__ import House
from models.Numbers import Numbers
from models.Trash import Trash


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
        self.rotation = 0
        self.mirror = False
        self.draw_items = draw_items

        Numbers.__init__(self, self.col, self.row)
        self.update()

    def random_starting_position(self):
        gc_initial_position = {"row": randint(
            0, MAP_HEIGHT - 1), "col": randint(0, MAP_WIDTH - 1)}
        while not self.road_positions[gc_initial_position["row"]][gc_initial_position["col"]]:
            gc_initial_position = {"row": randint(
                0, MAP_HEIGHT - 1), "col": randint(0, MAP_WIDTH - 1)}
        return gc_initial_position

    def update(self):
        draw, _, img = self.img_load(
            GARBAGE_COLLECTOR_IMAGE, 32)
        draw.line((6, 12) + (6, 40), (BLACK), 10)
        draw.line((17, 12) + (17, 40), (BLACK), 10)
        draw.line((28, 12) + (28, 40), (BLACK), 10)
        draw.line((39, 12) + (39, 40), (BLACK), 10)
        draw.line((6, self.get_fill(12, 40, self.mixed)) +
                  (6, 40), (128, 128, 128), 10)
        draw.line((17, self.get_fill(12, 40, self.paper)) +
                  (17, 40), (BLUE), 10)
        draw.line((28, self.get_fill(12, 40, self.glass)) +
                  (28, 40), (GREEN), 10)
        draw.line((39, self.get_fill(12, 40, self.plastic)) +
                  (39, 40), (YELLOW), 10)
        self.img_save(draw, img, self.rotation, self.mirror)

    def is_empty(self):
        if self.mixed == 0 and self.glass == 0 and self.paper == 0 and self.plastic == 0:
            return True
        else:
            return False

    def get_fill(self, base, full_val, trash):
        addable_range = full_val - base
        return full_val - ((trash / self.limit) * addable_range)

    def render(self):
        self.rect = pygame.Rect(
            self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.update()

    def move_up(self):
        result = False
        self.rotation = 90
        self.mirror = False
        if self.row > 0:
            if self.road_positions[self.row - 1][self.col]:
                self.row -= 1
                result = True

        return result

    def move_down(self):
        result = False
        self.rotation = 270
        self.mirror = False
        if self.row < MAP_HEIGHT - 1:
            if self.road_positions[self.row + 1][self.col]:
                self.row += 1
                result = True

        return result

    def move_left(self):
        result = False
        self.rotation = 0
        self.mirror = True
        if self.col > 0:
            if self.road_positions[self.row][self.col - 1]:
                self.col -= 1
                result = True

        return result

    def move_right(self):
        result = False
        self.rotation = 0
        self.mirror = False
        if self.col < MAP_WIDTH - 1:
            if self.road_positions[self.row][self.col + 1]:
                self.col += 1
                result = True

        return result

    def pick_trash(self):
        if self.mixed == self.limit and self.glass == self.limit and \
                self.paper == self.limit and self.plastic == self.limit:
            return

        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and \
                    field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, House):
                    for trash_type in TRASH_TYPES:
                        gc_trash, house_trash = getattr(
                            self, trash_type), getattr(item, trash_type)
                        if house_trash and gc_trash < self.limit:
                            if gc_trash + house_trash > self.limit:
                                house_trash = self.limit - gc_trash
                            item.get_trash(trash_type=trash_type,
                                           queried_ammount=house_trash)
                            setattr(self, trash_type, gc_trash + house_trash)

    def leave_trash(self):
        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and \
                    field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, Trash):
                    if item.trash_type in TRASH_TYPES:
                        trash_ammount = getattr(self, item.trash_type)
                        if trash_ammount:
                            item.put_trash(trash_ammount)
                            setattr(self, item.trash_type, 0)
                            break
