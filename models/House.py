import pygame
from config import CELL_SIZE


class House (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.mixed = 5
        self.paper = 5
        self.glass = 5
        self.plastic = 5
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/house.jpg"), (CELL_SIZE, CELL_SIZE))

    def get_mixed(self):
        if self.mixed > 0:
            self.mixed -= 1
            return True
        else:
            return False

    def get_paper(self):
        if self.paper > 0:
            self.paper -= 1
            return True
        else:
            return False

    def get_glass(self):
        if self.glass > 0:
            self.glass -= 1
            return True
        else:
            return False

    def get_plastic(self):
        if self.plastic > 0:
            self.plastic -= 1
            return True
        else:
            return False
