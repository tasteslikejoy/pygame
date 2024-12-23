import pygame, sys
import random

pygame.init()

WIDTH, HEIGHT  = 800, 600
sc = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("QTE")
pygame.display.set_icon(pygame.image.load('images/logo.png'))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (5, 5, 5)

x = 100
y = HEIGHT // 2
xr = random.randint(0, 700)
velocity = 10
velocity_left = False
moving = True

rect1 = pygame.draw.rect(sc, BLACK, (xr, 395, 70, 10))
rect2 = pygame.draw.rect(sc, RED, (x, y, 10, 50))

while True:

    if moving and not velocity_left:
        x += velocity
        if x > WIDTH:
            velocity_left = True
    elif moving and velocity_left:
        x -= velocity
        if x < 0:
            velocity_left = False

    sc.fill(WHITE)
    pygame.draw.line(sc, BLACK, (0, 400), (800, 400))
    pygame.draw.rect(sc, BLACK, (xr, 395, 70, 10))
    pygame.draw.rect(sc, RED, (x, y, 10, 50))

    if rect1.colliderect(rect2):
        print("Прямоугольники пересекаются!")
    else:
        print("Прямоугольники не пересекаются.")

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            moving = False