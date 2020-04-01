import pygame
from config import CELL_SIZE, FONT, BLACK, BLUE, GREEN, YELLOW, HOUSE_IMAGE
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from models.Numbers import Numbers


class House (Numbers):
    def __init__(self, x, y):
        Numbers.__init__(self, x, y)
        self.mixed = 5
        self.paper = 5
        self.glass = 5
        self.plastic = 5
        self.img_update(HOUSE_IMAGE)

    def get_mixed(self):
        if self.mixed > 0:
            self.mixed -= 1
            self.img_update(HOUSE_IMAGE)
            return True
        else:
            return False

    def get_paper(self):
        if self.paper > 0:
            self.paper -= 1
            self.img_update(HOUSE_IMAGE)
            return True
        else:
            return False

    def get_glass(self):
        if self.glass > 0:
            self.glass -= 1
            self.img_update(HOUSE_IMAGE)
            return True
        else:
            return False

    def get_plastic(self):
        if self.plastic > 0:
            self.plastic -= 1
            self.img_update(HOUSE_IMAGE)
            return True
        else:
            return False
