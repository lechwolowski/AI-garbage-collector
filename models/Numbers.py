from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pygame
from config import CELL_SIZE, BLACK, BLUE, GREEN, YELLOW, FONT


class Numbers (pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.col = x
        self.row = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def img_load(self, image, font_size):
        img = Image.open(f"Resources/Images/{image}")
        img = img.resize((CELL_SIZE, CELL_SIZE))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT, font_size)
        return draw, font, img

    def img_save(self, draw, img, rotation=0, mirror=False):
        img = img.rotate(rotation)
        img = img.transpose(method=Image.FLIP_LEFT_RIGHT) if mirror else img
        data, size, mode = img.tobytes(), img.size, img.mode
        self.image = pygame.image.frombuffer(data, size, mode)
