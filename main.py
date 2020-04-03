import pygame
from models.Garbage_Collector import Garbage_Collector
from config import WINDOW_HEIGHT, WINDOW_WIDTH, TRASH_GLASS_IMAGE
from helpler import Render_Element
from knowledge import Knowledge
from models.Trash import Trash


pygame.init()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

display_group = pygame.sprite.Group()

draw_items = [[Render_Element(x, y) for x in range(16)] for y in range(10)]

for line in draw_items:
    for item in line:
        display_group.add(item)

gc = Garbage_Collector()

display_group.add(gc)

clock = pygame.time.Clock()


def refresh_screen():
    display_group.draw(WINDOW)
    display_group.draw(WINDOW)
    display_group.draw(WINDOW)
    display_group.draw(WINDOW)

    pygame.display.update()


pygame.display.update()
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
                know.show()

            refresh_screen()

            pygame.display.update()

    clock.tick(30)
