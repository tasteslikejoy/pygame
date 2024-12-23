import pygame as pg
import time, random

pg.init()

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

# display
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Размеры клетки (необходимо увеличить размеры экрана в ширину и высоту на 2 клетки)
CELL_SIZE = 50
CELL_PADDING = 2

# Количество клеток
CELLS_X = 16
CELLS_Y = 12

# Игровое поле
game_field = [[1 for _ in range(CELLS_X)] for _ in range(CELLS_Y)]


# Ход игрока
def move_player(player, new_position):
    x, y = new_position
    if 0 <= x < CELLS_X and 0 <= y < CELLS_Y and game_field[y][x] == 1:
        game_field[player[1]][player[0]] = 1  # Освободить старую клетку
        game_field[y][x] = 0  # Занять новую клетку
        return new_position
    return player


# Атака игрока
def attack_player(attacker, target, attack_type):
    if attack_type == "close":
        if abs(attacker[0] - target[0]) <= 1 and abs(attacker[1] - target[1]) <= 1:
            return True
    elif attack_type == "far":
        if abs(attacker[0] - target[0]) <= 3 and abs(attacker[1] - target[1]) <= 3:
            return True
    return False


FPC = 60
game_time = pg.time.Clock()


# Функция для хода NPC
def npc_move(player, target):
    dx = target[0] - player[0]
    dy = target[1] - player[1]
    go = random.randint(0, 1)
    if go == 1:
        if dx > 0:
            new_x = player[0] + random.randint(0, 1)
        elif dx < 0:
            new_x = player[0] - random.randint(0, 1)
        else:
            new_x = player[0]
        if dy > 0:
            new_y = player[1] + 1
        elif dy < 0:
            new_y = player[1] - 1
        else:
            new_y = player[1]
    else:
        if dx > 0:
            new_x = player[0] + 1
        elif dx < 0:
            new_x = player[0] - 1
        else:
            new_x = player[0]
        if dy > 0:
            new_y = player[1] + random.randint(0, 1)
        elif dy < 0:
            new_y = player[1] - random.randint(0, 1)
        else:
            new_y = player[1]

    return move_player(player, (new_x, new_y))


# Игроки
player1 = (0, 3)
player2 = (0, 6)


# NPC
npc1 = (CELLS_X - 1, 4)
npc2 = (CELLS_X - 1, 7)


# Здоровье игроков
player1_health = 100
player2_health = 100
player1_live = True
player2_live = True


# Здоровье NPC
npc1_health = 100
npc2_health = 100
npc1_live = True
npc2_live = True


# Размер шрифта
font = pg.font.Font(None, 25)


# Основной цикл игры
running = True # Флаг основного цикла игры
game_over = False # Флаг GAME OVER
current_turn = 1 # Определение очереди хода???

while running:

    # Обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


        # Перемещение игрока 1 с помощью мыши
        elif event.type == pg.MOUSEBUTTONDOWN and current_turn == 1:
            if player1_live:
                mouse_pos = pg.mouse.get_pos()
                new_x = mouse_pos[0] // CELL_SIZE
                new_y = mouse_pos[1] // CELL_SIZE
                if abs(new_x - player1[0]) <= 1 and abs(new_y - player1[1]) <= 1:
                    new_position = (new_x, new_y)
                    if move_player(player1, new_position) != player1:
                        player1 = new_position
                        current_turn = 2
            else:
                current_turn = 2


        #Атака первого игрока
        elif event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_a] and current_turn == 1:  # Ближняя атака
            if player1_live:
                if attack_player(player1, npc1, "close"):
                    print("Игрок 1 атакует NPC1 ближней атакой")
                    npc1_health -= 20
                elif attack_player(player1, npc2, "close"):
                    print("Игрок 1 атакует NPC2 ближней атакой")
                    npc2_health -= 20
                current_turn = 2
            else:
                current_turn = 2
        elif event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_d] and current_turn == 1:  # Дальняя атака
            if player1_live:
                if attack_player(player1, npc1, "far"):
                    print("Игрок 1 атакует NPC1 дальней атакой")
                    npc1_health -= 10
                elif attack_player(player1, npc2, "far"):
                    print("Игрок 1 атакует NPC2 дальней атакой")
                    npc2_health -= 10
                current_turn = 2
            else:
                current_turn = 2


        # Перемещение игрока 2 с помощью мыши
        elif event.type == pg.MOUSEBUTTONDOWN and current_turn == 2:
            if player2_live:
                mouse_pos = pg.mouse.get_pos()
                new_x = mouse_pos[0] // CELL_SIZE
                new_y = mouse_pos[1] // CELL_SIZE
                if abs(new_x - player2[0]) <= 1 and abs(new_y - player2[1]) <= 1:
                    new_position = (new_x, new_y)
                    if move_player(player2, new_position) != player2:
                        player2 = new_position
                        current_turn = 3
            else:
                current_turn = 3


        # Атака второго игрока
        elif event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_a] and current_turn == 2:  # Ближняя атака
            if player2_live:
                print('Ok')
                if attack_player(player2, npc1, "close"):
                    print("Игрок 2 атакует NPC1 ближней атакой")
                    npc1_health -= 20
                elif attack_player(player2, npc2, "close"):
                    print("Игрок 2 атакует NPC2 ближней атакой")
                    npc2_health -= 20
                current_turn = 3
            else:
                current_turn = 3
        elif event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_d] and current_turn == 2: # Дальняя атака
            if player2_live:
                if attack_player(player2, npc1, "far"):
                    print("Игрок 2 атакует NPC1 дальней атакой")
                    npc1_health -= 10
                elif attack_player(player2, npc2, "far"):
                    print("Игрок 2 атакует NPC2 дальней атакой")
                    npc2_health -= 10
                current_turn = 3
            else:
                current_turn = 3


        # Ход NPC
        if current_turn == 3:
            if player1_live:
                if attack_player(npc1, player1,"far"):
                    print("NPC1 атакует игрока 1")
                    player1_health -= 10
                    if player1_health <= 0:
                        player1_live = False
                else:
                    npc1 = npc_move(npc1, player1)
            else:
                if attack_player(npc1, player2,"far"):
                    print("NPC1 атакует игрока 2")
                    player2_health -= 10
                    if player2_health <= 0:
                        player2_live = False
                else:
                    npc1 = npc_move(npc1, player2)
            current_turn = 4

        # Атака NPC
        elif current_turn == 4:
            # time.sleep(1)
            if player2_live:
                if attack_player(npc2, player2, "far"):
                    print("NPC2 атакует игрока 2")
                    player2_health -= 10
                    if player2_health <= 0:
                        player2_live = False
                else:
                    npc2 = npc_move(npc2, player2)
            else:
                if attack_player(npc2, player1, "far"):
                    print("NPC2 атакует игрока 1")
                    player1_health -= 10
                    if player1_health <= 0:
                        player1_live = False
                else:
                    npc2 = npc_move(npc2, player1)
            current_turn = 1


    # Отрисовка игрового поля
    for y in range(CELLS_Y):
        for x in range(CELLS_X):
            cell_rect = pg.Rect(x * CELL_SIZE + CELL_PADDING, y * CELL_SIZE + CELL_PADDING,
                               CELL_SIZE - CELL_PADDING * 2, CELL_SIZE - CELL_PADDING * 2)
            pg.draw.rect(screen, GREEN, cell_rect)


    # Отрисовка игроков и NPC
    pg.draw.circle(screen, BLACK,
                   (player1[0] * CELL_SIZE + CELL_SIZE // 2, player1[1] * CELL_SIZE + CELL_SIZE // 2),
                   CELL_SIZE // 4)
    pg.draw.circle(screen, RED,
                   (player2[0] * CELL_SIZE + CELL_SIZE // 2, player2[1] * CELL_SIZE + CELL_SIZE // 2),
                   CELL_SIZE // 4)
    pg.draw.circle(screen, BROWN, (npc1[0] * CELL_SIZE + CELL_SIZE // 2, npc1[1] * CELL_SIZE + CELL_SIZE // 2),
                   CELL_SIZE // 4)
    pg.draw.circle(screen, BROWN, (npc2[0] * CELL_SIZE + CELL_SIZE // 2, npc2[1] * CELL_SIZE + CELL_SIZE // 2),
                   CELL_SIZE // 4)


    # Отрисовка информации о здоровье
    if player1_live:
        text = font.render(f"Player 1 Health: {player1_health}", True, WHITE)
    else:
        text = font.render(f"Player 1 Health: DIED", True, WHITE)
    screen.blit(text, (10, 10))
    if player2_live:
        text = font.render(f"Player 2 Health: {player2_health}", True, WHITE)
    else:
        text = font.render(f"Player 2 Health: DIED", True, WHITE)
    screen.blit(text, (10, 40))
    text = font.render(f"NPC 1 Health: {npc1_health}", True, WHITE)
    screen.blit(text, (10, 70))
    text = font.render(f"NPC 2 Health: {npc2_health}", True, WHITE)
    screen.blit(text, (10, 100))


    if not player1_live and not player2_live:
        running = False


    pg.display.flip()
    game_time.tick(FPC)


pg.quit()


# В этом коде мы добавили функцию attack_player(), которая проверяет, находится ли игрок в пределах 3 клеток от другого игрока. Если это так, то при перемещении игрока происходит атака на другого игрока.
#
# Также мы добавили переменные player1_health, player2_health, npc1_health и npc2_health для хранения здоровья игроков и NPC. При атаке здоровье уменьшается на 10 единиц.
#
# В основном цикле игры мы добавили проверку, находится ли игрок в пределах 3 клеток от NPC. Если да, то NPC атакует игрока, уменьшая его здоровье.
#
# Теперь при перемещении игроков и ходе NPC происходит проверка на атаку, и информация о здоровье отображается на экране.