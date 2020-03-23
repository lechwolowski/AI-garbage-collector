import pygame

pygame.init()

screen = pygame.display.set_mode((320, 200))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
            if event.key == pygame.K_RIGHT:
                print("Right")
            if event.key == pygame.K_UP:
                print("Up")
            if event.key == pygame.K_DOWN:
                print("Down")
