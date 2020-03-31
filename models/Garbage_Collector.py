import pygame
from config import CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from random import randint
from config import MAP
from models.House import House


class Garbage_Collector(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.road_positions = {row_index: {
            col_index: (True if MAP[row_index][col_index] == "Road" else False)
            for col_index in MAP[row_index]} for row_index in MAP}

        gc_initial_position = {"row": randint(0, 9), "col": randint(0, 15)}
        while not self.road_positions[gc_initial_position["row"]][gc_initial_position["col"]]:
            # print(gc_initial_position)
            gc_initial_position = {"row": randint(0, 9), "col": randint(0, 15)}

        self.col = gc_initial_position["col"]
        self.row = gc_initial_position["row"]
        self.rect = pygame.Rect(
            self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/garbage-collector.png"), (CELL_SIZE, CELL_SIZE))

        self.mixed = 0
        self.paper = 0
        self.glass = 0
        self.plastic = 0
        self.limit = 10

    def set_rect(self, mirror):
        self.rect = pygame.Rect(
            self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if mirror:
            self.image = pygame.transform.flip(pygame.transform.rotate(
                pygame.transform.scale(pygame.image.load(
                    "Resources/Images/garbage-collector.png"), (CELL_SIZE, CELL_SIZE)
                ),
                self.rotation
            ), True, False)
        else:
            self.image = pygame.transform.rotate(
                pygame.transform.scale(pygame.image.load(
                    "Resources/Images/garbage-collector.png"), (CELL_SIZE, CELL_SIZE)
                ),
                self.rotation
            )

    def move_up(self):
        self.rotation = 90
        if self.row > 0:
            if self.road_positions[self.row - 1][self.col]:
                self.row -= 1
        self.set_rect(False)

    def move_down(self):
        self.rotation = 270
        if self.row < MAP_HEIGHT - 1:
            if self.road_positions[self.row + 1][self.col]:
                self.row += 1
        self.set_rect(False)

    def move_left(self):
        self.rotation = 0
        if self.col > 0:
            if self.road_positions[self.row][self.col - 1]:
                self.col -= 1
        self.set_rect(True)

    def move_right(self):
        self.rotation = 0
        if self.col < MAP_WIDTH - 1:
            if self.road_positions[self.row][self.col + 1]:
                self.col += 1
        self.set_rect(False)

    def trash_flow(self, draw_items):
        to_check = [
            {"col": self.col - 1, "row": self.row},
            {"col": self.col + 1, "row": self.row},
            {"col": self.col, "row": self.row - 1},
            {"col": self.col, "row": self.row + 1},
        ]
        for field in to_check:
            if field["row"] >= 0 and field["row"] < MAP_HEIGHT and field["col"] >= 0 and field["col"] < MAP_WIDTH:
                if isinstance(draw_items[field["row"]][field["col"]], House):

                    mixed = True
                    while mixed and self.mixed < self.limit:
                        print(
                            {"mixed": draw_items[field["row"]][field["col"]].mixed})
                        mixed = draw_items[field["row"]
                                           ][field["col"]].get_mixed()
                        if mixed:
                            self.mixed += 1

                    paper = True
                    while paper and self.paper < self.limit:
                        paper = draw_items[field["row"]
                                           ][field["col"]].get_paper()
                        if paper:
                            self.paper += 1

                    glass = True
                    while glass and self.glass < self.limit:
                        glass = draw_items[field["row"]
                                           ][field["col"]].get_glass()
                        if glass:
                            self.glass += 1

                    plastic = True
                    while plastic and self.plastic < self.limit:
                        plastic = draw_items[field["row"]
                                             ][field["col"]].get_plastic()
                        if plastic:
                            self.plastic += 1
