import pygame
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH, TRASH_GLASS_IMAGE, CELL_SIZE, MAP_HEIGHT, MAP_WIDTH
from helpler import Render_Element
from Knowledge import Knowledge
from models.Trash import Trash


pygame.init()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

display_group = pygame.sprite.Group()

draw_items = {(x, y): Render_Element(x, y)
              for x in range(16) for y in range(10)}

for item in draw_items:
    display_group.add(draw_items[item])

gc = Garbage_Collector()

display_group.add(gc)

clock = pygame.time.Clock()


def refresh_screen():
    col, row = gc.col, gc.row
    for _ in range(4):
        for i in range(-1, 2):
            if row + i >= 0 and row + i < MAP_HEIGHT:
                WINDOW.blit(draw_items[col, row + i].image,
                            (col * CELL_SIZE, (row + i) * CELL_SIZE))
            if col + i >= 0 and col + i < MAP_WIDTH:
                WINDOW.blit(draw_items[col + i, row].image,
                            ((col + i) * CELL_SIZE, row * CELL_SIZE))
    for _ in range(4):
        WINDOW.blit(gc.image, (col * CELL_SIZE, row * CELL_SIZE))
    pygame.display.update()


for _ in range(4):
    display_group.draw(WINDOW)
pygame.display.flip()
know = Knowledge(draw_items, gc)
refresh_screen()
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gc.move_left()
            if event.key == pygame.K_RIGHT:
                gc.move_right()
            if event.key == pygame.K_UP:
                gc.move_up()
            if event.key == pygame.K_DOWN:
                gc.move_down()
            if event.key == pygame.K_SPACE:
                gc.trash_flow(draw_items)
                know.update()
                know.show()

            refresh_screen()

    clock.tick(30)
