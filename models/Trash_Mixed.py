import pygame
from config import CELL_SIZE


class Trash_Mixed (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/trash-mixed.png"), (CELL_SIZE, CELL_SIZE))
        self.trash = 0

    def put_trash(self):
        self.trash += 1