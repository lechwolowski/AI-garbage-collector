import pygame
from config import CELL_SIZE, FONT, BLACK, BLUE, GREEN, YELLOW, TRASH_MIXED_IMAGE
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from models.Numbers import Numbers


class Trash_Mixed (Numbers):
    def __init__(self, x, y):
        Numbers.__init__(self, x, y)
        self.trash = 0
        self.text_update()
        self.img_update(TRASH_MIXED_IMAGE, self.texts)

    def text_update(self):
        self.texts = [
            {"quantity": str(self.trash), "color": BLACK,
             "position": (30, 30)},
        ]

    def put_trash(self):
        self.trash += 1
        self.text_update()
        self.img_update(TRASH_MIXED_IMAGE, self.texts)
