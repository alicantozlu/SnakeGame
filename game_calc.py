import random
from highscore import *


def check_ahead(ekran, x, y):
    color = ekran.get_at((x, y))
    if color[0] == 35:
        return 'EAT'
    elif color[1] == 215:
        return 'BONUS'
    elif color[0] == 255 or color[2] == 205:
        return 'GAME_OVER'
    elif color[0] == 1:
        return 'KENAR_UST'
    elif color[0] == 2:
        return 'KENAR_ALT'
    elif color[0] == 3:
        return 'KENAR_SAG'
    elif color[0] == 4:
        return 'KENAR_SOL'
    elif color[0] == 0 and color[1] == 0 and color[2] == 0 or color[0] == 254:
        return 'NOTHING'

def first_food():
    return [50, 350]

def new_food(ekran):
    while True:
        x = random.randrange(42, 982, step=10)
        y = random.randrange(74, 682, step=10)
        if check_ahead(ekran, x, y) == 'NOTHING':
            return [x, y]


def game_pause(ekran):
    running = True
    renk = (8, 145, 3)
    font = pygame.font.Font(os.path.join('font.ttf'), 30)

    update_rect = pygame.Rect(150, 170, 760, 220)

    upper_border = pygame.Rect(150, 170, 760, 15)
    right_border = pygame.Rect(895, 185, 15, 200)
    left_border = pygame.Rect(150, 185, 15, 200)
    down_border = pygame.Rect(150, 370, 760, 15)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'CIKIS'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'CIKIS'
                else:
                    return 'DEVAM'

        pygame.draw.rect(pygame.display.set_mode([1024, 768]), (0, 0, 0), update_rect)

        ekran.blit(font.render("Devam Etmek İçin Bir Tuşa Basın", False, renk), (320, 230))
        ekran.blit(font.render("Çıkmak İçin ESC'ye Basın", False, renk), (350, 280))

        pygame.draw.rect(ekran, renk, upper_border)
        pygame.draw.rect(ekran, renk, right_border)
        pygame.draw.rect(ekran, renk, down_border)
        pygame.draw.rect(ekran, renk, left_border)
        pygame.display.update(update_rect)


def input_name(ekran):
    renk = (8, 145, 3)
    running = True
    clock = pygame.time.Clock()
    name = ""
    name_font = pygame.font.Font(os.path.join('font.ttf'), 50)
    name_border = pygame.Rect(380, 350, 320, 5)
    update_rect = pygame.Rect(150, 170, 760, 220)

    upper_border = pygame.Rect(150, 170, 760, 15)
    right_border = pygame.Rect(895, 185, 15, 200)
    left_border = pygame.Rect(150, 185, 15, 200)
    down_border = pygame.Rect(150, 370, 760, 15)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'CIK'
                elif event.key == pygame.K_RETURN:
                    if name:
                        return name.upper()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                else:
                    if not len(name) > 12:
                        name = name + event.unicode

        pygame.draw.rect(pygame.display.set_mode([1024, 768]), (0, 0, 0), update_rect)
        ekran.blit(name_font.render("Yeni Rekor!", False, renk), (420, 200))
        ekran.blit(name_font.render("isim: ", False, renk), (180, 300))
        ekran.blit(name_font.render(name.upper(), False, renk), (390, 300))
        pygame.draw.rect(ekran, renk, name_border)
        pygame.draw.rect(ekran, renk, upper_border)
        pygame.draw.rect(ekran, renk, right_border)
        pygame.draw.rect(ekran, renk, down_border)
        pygame.draw.rect(ekran, renk, left_border)
        pygame.display.update(update_rect)
        clock.tick(25)
