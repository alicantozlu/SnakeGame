from pygame import key
from pygame.constants import K_LSHIFT

from game_calc import *


def game_1(ekran, clock):
    running = True

    yilan_renk = (255, 255, 255)
    renk = (0, 0, 205)

    border_yatay = 1000
    upper_border_yatay_x = 12
    upper_border_yatay_y = 44
    lower_border_yatay_x = 12
    lower_border_yatay_y = 694
    border_dikey = 648
    right_border_dikey_x = 992
    right_border_dikey_y = 60
    left_border_dikey_x = 12
    left_border_dikey_y = 60

    upper_border = pygame.Rect(upper_border_yatay_x, upper_border_yatay_y, border_yatay, 20)
    down_border = pygame.Rect(lower_border_yatay_x, lower_border_yatay_y, border_yatay, 20)
    right_border = pygame.Rect(right_border_dikey_x, right_border_dikey_y, 20, border_dikey)
    left_border = pygame.Rect(left_border_dikey_x, left_border_dikey_y, 20, border_dikey)

    snake = [(512, 344), (512, 354), (512, 364), (512, 374), (512, 384)]
    direction = 'UP'
    bonus_timer = 0
    food = new_food(ekran)
    bonus = False
    eaten = True
    eaten_cooldown = 1
    x_change = 0
    y_change = 0
    score = 0

    countdown = True

    up_pressed = False
    right_pressed = False
    down_pressed = False
    left_pressed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    durum = game_pause(ekran)
                    if durum == 'CIKIS':
                        running = False
                if event.key == pygame.K_UP and not direction == 'DOWN' and not right_pressed and not left_pressed:
                    direction = 'UP'
                    up_pressed = True
                elif event.key == pygame.K_DOWN and not direction == 'UP' and not right_pressed and not left_pressed:
                    direction = 'DOWN'
                    down_pressed = True
                elif event.key == pygame.K_RIGHT and not direction == 'LEFT' and not up_pressed and not down_pressed:
                    direction = 'RIGHT'
                    right_pressed = True
                elif event.key == pygame.K_LEFT and not direction == 'RIGHT' and not up_pressed and not down_pressed:
                    direction = 'LEFT'
                    left_pressed = True

        up_pressed = False
        right_pressed = False
        down_pressed = False
        left_pressed = False

        keys = key.get_pressed()

        if direction == 'RIGHT':
            x_change = 10
            y_change = 0
            if keys[K_LSHIFT]:
                x_change = 20
                y_change = 0

        elif direction == 'LEFT':
            x_change = -10
            y_change = 0
            if keys[K_LSHIFT]:
                x_change = -20
                y_change = 0

        elif direction == 'UP':
            x_change = 0
            y_change = -10
            if keys[K_LSHIFT]:
                x_change = 0
                y_change = -20

        elif direction == 'DOWN':
            x_change = 0
            y_change = 10
            if keys[K_LSHIFT]:
                x_change = 0
                y_change = 20

        status = check_ahead(ekran, snake[0][0] + x_change, snake[0][1] + y_change)

        if status == 'NOTHING':
            snake.insert(0, (snake[0][0] + x_change, snake[0][1] + y_change))

        if status == 'EAT':
            eaten = True
            eaten_cooldown += 2
            food = new_food(ekran)
            score += 1
            if random.randint(1, 5) == 5 and not bonus:
                bonus = new_food(ekran)
                bonus_timer = 5

        if status == 'BONUS':
            bonus = False
            score += 6
            eaten_cooldown += 2

        if not eaten and eaten_cooldown == 0:
            snake = snake[0:-1]
        else:
            eaten = False
            eaten_cooldown = eaten_cooldown - 1

        if status == 'GAME_OVER':
            return score

        if bonus_timer:
            bonus_timer = bonus_timer - (clock.get_time() / 1000)
            if bonus_timer <= 0:
                bonus = False
                bonus_timer = 0

        ekran.fill((0, 0, 0))

        pygame.draw.rect(ekran, renk, upper_border)
        pygame.draw.rect(ekran, renk, right_border)
        pygame.draw.rect(ekran, renk, left_border)
        pygame.draw.rect(ekran, renk, down_border)
        pygame.draw.rect(ekran, (35, 142, 35), pygame.Rect(food[0], food[1], 10, 10))

        font = pygame.font.Font(os.path.join('font.ttf'), 28)

        if bonus:
            pygame.draw.rect(ekran, (255, 215, 0), pygame.Rect(bonus[0], bonus[1], 10, 10))
            ekran.blit(font.render(str(round(bonus_timer, 1)), True, (254, 254, 0)), (200, 8))

        ekran.blit(font.render("Skor: " + str(score), False, (254, 254, 0)), (900, 8))

        for dot in snake:
            pygame.draw.rect(ekran, yilan_renk, pygame.Rect(dot[0], dot[1], 10, 10))

        pygame.display.update()

        countdown_font = pygame.font.Font(os.path.join('font.ttf'), 50)

        if countdown:
            update_rect = pygame.Rect(500, 350, 50, 50)
            countdown = False
            for i in range(3, 0, -1):
                pygame.draw.rect(ekran, (0, 0, 0), update_rect)
                ekran.blit(countdown_font.render(str(i), False, renk), (500, 350))
                pygame.display.update(update_rect)
                pygame.time.delay(1000)

        clock.tick(25)
