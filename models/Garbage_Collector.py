import pygame
from config import CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from random import randint


class Garbage_Collector(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.road_positions = {row_index: {
            col_index: True for col_index in range(16)} for row_index in range(10)}

        for row_index in self.road_positions:
            for col_index in self.road_positions[row_index]:
                self.road_positions[row_index][0] = False
                self.road_positions[row_index][2] = False
                self.road_positions[row_index][3] = False
                self.road_positions[row_index][5] = False
                self.road_positions[row_index][7] = False
                self.road_positions[row_index][8] = False

        gc_initial_position = {"row": randint(0, 9), "col": randint(0, 15)}
        while not self.road_positions[gc_initial_position["row"]][gc_initial_position["col"]]:
            # print(gc_initial_position)
            gc_initial_position = {"row": randint(0, 9), "col": randint(0, 15)}

        self.col = gc_initial_position["col"]
        self.row = gc_initial_position["row"]
        self.rect = pygame.Rect(
            self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/white.png"), (CELL_SIZE, CELL_SIZE))

    def set_rect(self):
        self.rect = pygame.Rect(
            self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.rotate(
            pygame.transform.scale(pygame.image.load(
                "Resources/white.png"), (CELL_SIZE, CELL_SIZE)
            ),
            self.rotation
        )

    def move_up(self):
        if self.row > 0:
            if self.road_positions[self.row - 1][self.col]:
                self.rotation = 0
                self.row -= 1
                self.set_rect()

    def move_down(self):
        if self.row < MAP_HEIGHT - 1:
            if self.road_positions[self.row + 1][self.col]:
                self.rotation = 180
                self.row += 1
                self.set_rect()

    def move_left(self):
        if self.col > 0:
            if self.road_positions[self.row][self.col - 1]:
                self.rotation = 90
                self.col -= 1
                self.set_rect()

    def move_right(self):
        if self.col < MAP_WIDTH - 1:
            if self.road_positions[self.row][self.col + 1]:
                self.rotation = 270
                self.col += 1
                self.set_rect()
