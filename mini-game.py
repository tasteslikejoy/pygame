import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT  = 800, 600
sc = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame.RESIZABLE ???

pygame.display.set_caption("QTE")
pygame.display.set_icon(pygame.image.load('images/logo.png'))

clock = pygame.time.Clock()
FPS = 30

line = pygame.Surface((800, 1))
line.fill('black')
lx, ly = 0, 400

rect1 = pygame.image.load('images/Прямоугольник 1.png')
xr = random.randint(0, 700)
rect_1 = rect1.get_rect()

rect2 = pygame.image.load('images/Прямоугольник 2.png')
rx, ry = 10, 300
rect_2_speed = 10
move_right = True

running = True
while running:

    sc.fill(('white'))
    sc.blit(line, (0, 400))
    sc.blit(rect1, (xr, 395))
    sc.blit(rect2, (rx, ry))

    if move_right:
        rx += rect_2_speed
        if rx > 790:
            move_right = False
    else:
        rx -= rect_2_speed
        if rx < 0:
            rx += rect_2_speed
            move_right = True

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            move_right = False




