import pygame

pygame.init()

screen = pygame.display.set_mode((320, 200))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False