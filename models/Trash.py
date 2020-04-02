import pygame
from config import CELL_SIZE
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from models.Numbers import Numbers


class Trash (Numbers):
    def __init__(self, x, y, trash_type, image_name):
        Numbers.__init__(self, x, y)
        self.trash_type = trash_type
        self.image_name = image_name
        self.trash = 0
        self.update()

    def update(self):
        draw, font, img = self.img_load(self.image_name, 32)
        w, h = draw.textsize(str(self.trash), font=font)
        draw.text(((CELL_SIZE - w) / 2, (CELL_SIZE - h)
                   * 2 / 3), str(self.trash), font=font)
        self.img_save(draw, img)

    def put_trash(self):
        self.trash += 1
        self.update()
