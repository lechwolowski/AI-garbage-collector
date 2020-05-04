import pygame
from config import CELL_SIZE, FONT, BLACK, BLUE, GREEN, YELLOW, HOUSE_IMAGE
from random import randint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from models.Numbers import Numbers


class House (Numbers):
    def __init__(self, x, y):
        Numbers.__init__(self, x, y)
        self.zero = 0
        self.limit = 9
        self.mixed = randint(0, self.limit)
        self.paper = randint(0, self.limit)
        self.glass = randint(0, self.limit)
        self.plastic = randint(0, self.limit)
        self.update()

    def update(self):
        draw, font, img = self.img_load(HOUSE_IMAGE, 32)
        font = ImageFont.truetype(FONT, 14)
        w, h = draw.textsize(str(self.mixed), font=font)
        draw.text((19, 24), str(self.mixed), BLACK, font=font)
        draw.text((37, 24), str(self.paper), BLUE, font=font)
        draw.text((19, 42), str(self.glass), GREEN, font=font)
        draw.text((37, 42), str(self.plastic), YELLOW, font=font)
        self.img_save(draw, img)

    def is_empty(self):
        if self.mixed == 0 and self.glass == 0 and self.paper == 0 and self.plastic == 0:
            return True
        else:
            return False

    def get_trash(self, trash_type, queried_ammount):
        current_ammount = getattr(self, trash_type)
        if current_ammount >= queried_ammount:
            setattr(self, trash_type, current_ammount - queried_ammount)
            self.update()
