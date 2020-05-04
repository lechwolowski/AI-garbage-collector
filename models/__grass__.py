import pygame
from config import CELL_SIZE


class Grass(pygame.sprite.Sprite):
    def __init__(self, __x__, __y__):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            __x__ * CELL_SIZE, __y__ * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/grass.png"), (CELL_SIZE, CELL_SIZE))
