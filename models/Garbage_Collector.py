import pygame
from config import CELL_SIZE, MAP_HEIGHT, MAP_WIDTH, MAP, FONT, BLACK, BLUE, GREEN, YELLOW, GARBAGE_COLLECTOR_IMAGE
from random import randint
from models.House import House
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from models.Numbers import Numbers
from models.Trash import Trash


class Garbage_Collector(Numbers):
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
        draw, font, img = self.img_load(
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
        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        houses_around = False
        transfered = 0
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, House):
                    houses_around = True

                    mixed = True
                    while mixed and self.mixed < self.limit:
                        mixed = item.get_mixed()
                        if mixed:
                            self.mixed += 1
                            transfered += 1

                    paper = True
                    while paper and self.paper < self.limit:
                        paper = item.get_paper()
                        if paper:
                            self.paper += 1
                            transfered += 1

                    glass = True
                    while glass and self.glass < self.limit:
                        glass = item.get_glass()
                        if glass:
                            self.glass += 1
                            transfered += 1

                    plastic = True
                    while plastic and self.plastic < self.limit:
                        plastic = item.get_plastic()
                        if plastic:
                            self.plastic += 1
                            transfered += 1
        if houses_around:
            return transfered
        else:
            return -10

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
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and field["col"] >= 0 and field["col"] < MAP_WIDTH:
                item = self.draw_items[(field["col"], field["row"])]
                if isinstance(item, Trash):
                    trashes_around = True
                    if item.trash_type == "Mixed":
                        while self.mixed > 0:
                            item.put_trash()
                            self.mixed -= 1
                            transfered += 1
                    elif item.trash_type == "Paper":
                        while self.paper > 0:
                            item.put_trash()
                            self.paper -= 1
                            transfered += 1
                    elif item.trash_type == "Glass":
                        while self.glass > 0:
                            item.put_trash()
                            self.glass -= 1
                            transfered += 1
                    elif item.trash_type == "Plastic":
                        while self.plastic > 0:
                            item.put_trash()
                            self.plastic -= 1
                            transfered += 1

        if trashes_around:
            return transfered
        else:
            return -10
