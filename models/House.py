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
        self.mixed = randint(0, 2)
        self.paper = randint(0, 2)
        self.glass = randint(0, 2)
        self.plastic = randint(0, 2)
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

    def get_mixed(self):
        if self.mixed > 0:
            self.mixed -= 1
            self.update()

            return True
        else:
            return False

    def get_paper(self):
        if self.paper > 0:
            self.paper -= 1
            self.update()

            return True
        else:
            return False

    def get_glass(self):
        if self.glass > 0:
            self.glass -= 1
            self.update()

            return True
        else:
            return False

    def get_plastic(self):
        if self.plastic > 0:
            self.plastic -= 1
            self.update()

            return True
        else:
            return False
