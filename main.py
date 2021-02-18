import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from game_1 import game_1
from game_2 import game_2
from game_3 import game_3
from game_calc import *
from highscore import *

x = 500
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()

ekran_width = 1024
ekran_height = 768
ekran = pygame.display.set_mode([ekran_width, ekran_height])

pygame.display.set_caption('Yılan Oyunu')

menu_renk = (8, 145, 3)

nokta = pygame.Rect(320, 215, 8, 8)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                if nokta.top == 215:
                    nokta.move_ip(0, 200)
                else:
                    nokta.move_ip(0, -50)
            elif event.key == pygame.K_DOWN:
                if nokta.top == 415:
                    nokta.move_ip(0, -200)
                else:
                    nokta.move_ip(0, 50)
            elif event.key == pygame.K_RETURN:
                if nokta.top == 215:
                    score = game_1(ekran, clock)
                    if score and is_record(score):
                        name = input_name(ekran)
                        if name == 'CIK':
                            break
                        else:
                            new_record(score, name)
                            show_highscore(ekran)
                elif nokta.top == 265:
                    score = game_2(ekran, clock)
                    if score and is_record(score):
                        name = input_name(ekran)
                        if name == 'CIK':
                            break
                        else:
                            new_record(score, name)
                            show_highscore(ekran)
                elif nokta.top == 315:
                    score = game_3(ekran, clock)
                    if score and is_record(score):
                        name = input_name(ekran)
                        if name == 'CIK':
                            break
                        else:
                            new_record(score, name)
                            show_highscore(ekran)
                elif nokta.top == 365:
                    show_highscore(ekran)
                elif nokta.top == 415:
                    running = False
        else:
            running = True

    baslik_font = pygame.font.Font(os.path.join('font.ttf'), 120)
    yazi_font = pygame.font.Font(os.path.join('font.ttf'), 40)

    ekran.fill((0, 0, 0))

    ekran.blit(baslik_font.render("Yılan Oyunu", True, menu_renk), (190, 15))
    ekran.blit(yazi_font.render("Mod 1", True, menu_renk), (350, 200))
    ekran.blit(yazi_font.render("Mod 2", True, menu_renk), (350, 250))
    ekran.blit(yazi_font.render("Mod 3", True, menu_renk), (350, 300))
    ekran.blit(yazi_font.render("Skor Tablosu", True, menu_renk), (350, 350))
    ekran.blit(yazi_font.render("Çıkış", True, menu_renk), (350, 400))

    pygame.draw.rect(ekran, menu_renk, nokta)
    pygame.display.update()
