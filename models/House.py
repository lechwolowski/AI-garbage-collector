import pygame
from config import CELL_SIZE
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class House (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.mixed = 5
        self.paper = 5
        self.glass = 5
        self.plastic = 5
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        self.img_update()

    def img_update(self):
        img = Image.open("Resources/Images/house.jpg")
        img = img.resize((CELL_SIZE, CELL_SIZE))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("FiraCode-Bold.otf", 16)
        draw.text((20, 20), str(self.glass), (0, 0, 0), font=font)
        data, size, mode = img.tobytes(), img.size, img.mode
        self.image = pygame.image.frombuffer(data, size, mode)

    def get_mixed(self):
        if self.mixed > 0:
            self.mixed -= 1
            self.img_update()
            return True
        else:
            return False

    def get_paper(self):
        if self.paper > 0:
            self.paper -= 1
            self.img_update()
            return True
        else:
            return False

    def get_glass(self):
        if self.glass > 0:
            self.glass -= 1
            self.img_update()
            return True
        else:
            return False

    def get_plastic(self):
        if self.plastic > 0:
            self.plastic -= 1
            self.img_update()
            return True
        else:
            return False
