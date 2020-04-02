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
        self.update()

    #     self.texts = [
    #         {"quantity": str(self.mixed), "color": BLACK, "position": (5, 0)},
    #         {"quantity": str(self.paper), "color": BLUE, "position": (20, 0)},
    #         {"quantity": str(self.glass), "color": GREEN, "position": (34, 0)},
    #         {"quantity": str(self.plastic), "color": YELLOW,
    #          "position": (49, 0)}
    #     ]

    def update(self):
        draw, font, img = self.img_load(HOUSE_IMAGE, 32)
        w, h = draw.textsize(str(self.mixed), font=font)
        draw.text(((CELL_SIZE - w) / 2, (CELL_SIZE - h)
                   * 2 / 3), str(self.mixed), font=font)
        self.img_save(draw, img)

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
