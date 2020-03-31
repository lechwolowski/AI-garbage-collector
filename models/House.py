import pygame
from config import CELL_SIZE


class House (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.trash = 5
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/house.jpg"), (CELL_SIZE, CELL_SIZE))

    def get_trash(self):
        if self.trash > 0:
            self.trash -= 1
            return True
        else:
            return False
