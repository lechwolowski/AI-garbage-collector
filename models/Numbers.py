from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pygame
from config import CELL_SIZE, BLACK, BLUE, GREEN, YELLOW, FONT


class Numbers (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def img_update(self, image):
        img = Image.open(f"Resources/Images/{image}")
        img = img.resize((CELL_SIZE, CELL_SIZE))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT, 16)
        texts = [
            {"quantity": str(self.mixed), "color": BLACK},
            {"quantity": str(self.paper), "color": BLUE},
            {"quantity": str(self.glass), "color": GREEN},
            {"quantity": str(self.plastic), "color": YELLOW}
        ]
        step = CELL_SIZE / 4 - 1
        position = 4
        for txt in texts:
            draw.text((position, 0), txt["quantity"],
                      txt["color"], font=font)
            position += step
        data, size, mode = img.tobytes(), img.size, img.mode
        self.image = pygame.image.frombuffer(data, size, mode)
