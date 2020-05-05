from config import CELL_SIZE
from models.__numbers__ import Numbers


class Trash(Numbers):
    def __init__(self, x, y, trash_type):
        Numbers.__init__(self, x, y)
        self.trash_type = trash_type.lower()
        self.image_name = f"trash-{trash_type.lower()}.png"
        self.trash = 0
        self.update()

    def update(self):
        draw, font, img = self.img_load(self.image_name, 32)
        __w__, __h__ = draw.textsize(str(self.trash), font=font)
        draw.text(((CELL_SIZE - __w__) / 2, (CELL_SIZE - __h__)
                   * 2 / 3), str(self.trash), font=font)
        self.img_save(img)

    def put_trash(self, ammount=1):
        self.trash += ammount
        self.update()
