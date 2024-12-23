import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT  = 800, 600
sc = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame.RESIZABLE ???

pygame.display.set_caption("QTE")
pygame.display.set_icon(pygame.image.load('images/logo.png'))

clock = pygame.time.Clock()
FPS = 10

objects_list = [
    pygame.image.load('imagesQWEASD/a.png').convert_alpha(),
    pygame.image.load('imagesQWEASD/d.png').convert_alpha(),
    pygame.image.load('imagesQWEASD/e.png').convert_alpha(),
    pygame.image.load('imagesQWEASD/q.png').convert_alpha(),
    pygame.image.load('imagesQWEASD/s.png').convert_alpha(),
    pygame.image.load('imagesQWEASD/w.png').convert_alpha()
]

count = 0

label = pygame.font.SysFont('arial', 50)
reset_label = label.render(('RESET'), True, ('white'))
reset_label_rect = reset_label.get_rect(center=(WIDTH//2, HEIGHT//2))

game_time = 15
flag = True
game = True
running = True
while running:

    if game:
        game_time -= 1

        if count < 3 and flag:
            flag = False
            count_list = random.randint(0, 5)
            x_obj = random.randint(-300, 300)
            y_obj = random.randint(-200, 300)
            sc.blit(objects_list[count_list], (x_obj, y_obj))
        elif count == 3:
            game = False
            time.sleep(3)
            pygame.quit()
            sys.exit()
        elif game_time == 0:
            sc.blit(reset_label, reset_label_rect)
            game = False


    mouse = pygame.mouse.get_pos()
    if reset_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        count = 0
        game = True
        flag = True
        game_time = 50
        # Очистить экран и запустить игру по новой


    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and count_list == 0:
            flag = True
            count += 1
            game_time += 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and count_list == 1:
            flag = True
            count += 1
            game_time += 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and count_list == 2:
            flag = True
            count += 1
            game_time += 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q and count_list == 3:
            flag = True
            count += 1
            game_time += 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and count_list == 4:
            flag = True
            count += 1
            game_time += 5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and count_list == 5:
            flag = True
            count += 1
            game_time += 5
