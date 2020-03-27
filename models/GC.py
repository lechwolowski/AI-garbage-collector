import pygame
from config import CELL_SIZE, MAP_HEIGHT, MAP_WIDTH


class GC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/white.png"), (CELL_SIZE, CELL_SIZE))

    def set_rect(self):
        self.rect = pygame.Rect(
            self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def move_up(self):
        if self.y > 0:
            self.y -= 1
            self.set_rect()

    def move_down(self):
        if self.y < MAP_HEIGHT - 1:
            self.y += 1
            self.set_rect()

    def move_left(self):
        if self.x > 0:
            self.x -= 1
            self.set_rect()

    def move_right(self):
        if self.x < MAP_WIDTH - 1:
            self.x += 1
            self.set_rect()
