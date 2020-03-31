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
        if self.row > 0:
            if self.road_positions[self.row - 1][self.col]:
                self.rotation = 90
                self.row -= 1
                self.set_rect(False)

    def move_down(self):
        if self.row < MAP_HEIGHT - 1:
            if self.road_positions[self.row + 1][self.col]:
                self.rotation = 270
                self.row += 1
                self.set_rect(False)

    def move_left(self):
        if self.col > 0:
            if self.road_positions[self.row][self.col - 1]:
                pygame.transform.flip
                self.rotation = 0
                self.col -= 1
                self.set_rect(True)

    def move_right(self):
        if self.col < MAP_WIDTH - 1:
            if self.road_positions[self.row][self.col + 1]:
                self.rotation = 0
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
                    print(draw_items[field["row"]][field["col"]].trash)
                    print(draw_items[field["row"]][field["col"]].get_trash())
