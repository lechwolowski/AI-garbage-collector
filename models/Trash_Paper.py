import pygame
from models.Trash import Trash
from config import CELL_SIZE

'''
class Trash_Paper (pygame.sprite.Sprite, Trash):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/trash-paper.png"), (CELL_SIZE, CELL_SIZE))
        self.trash = 0
'''
class Trash_Paper (pygame.sprite.Sprite, Trash):
    def __init__(self, x, y):
        super().__init__(self,x,y)   
        self.image = pygame.transform.scale(pygame.image.load(
            "Resources/Images/trash-paper.png"), (CELL_SIZE, CELL_SIZE))