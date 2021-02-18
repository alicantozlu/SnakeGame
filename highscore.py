import os
import pygame


def show_highscore(ekran):
    running = True

    hs_font = pygame.font.Font(os.path.join('font.ttf'), 120)
    name_font = pygame.font.Font(os.path.join('font.ttf'), 50)
    renk = (8, 145, 3)
    ekran.fill((0, 0, 0))

    ekran.blit(hs_font.render("SKOR TABLOSU", False, renk), (100, 20))
    hs = get_highscore()
    ypos = 200
    if len(hs) == 0:
        ekran.blit(name_font.render('-', False, renk), (450, 200))
    for i in range(0, len(hs)):
        ekran.blit(name_font.render(str(i + 1) + '. ' + hs[i][0], False, renk), (300, ypos))
        ekran.blit(name_font.render(str(hs[i][1]), False, renk), (700, ypos))
        ypos += 50
    pygame.display.update()

    while running:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    running = False


def get_highscore():
    file = open('hs.dat', 'r')
    temp = file.read()
    file.close()
    data = temp.split(",")
    result = []
    for i in range(0, len(data) - 1, 2):
        result.append((data[i], int(data[i + 1])))
    return result


def write_highscore(hs):
    file = open('hs.dat', 'w')
    for i in hs:
        data = i[0] + ',' + str(i[1]) + ','
        file.write(data)
    file.close()


def is_record(score):
    hs = get_highscore()
    for i in range(len(hs)):
        if score > hs[i][1]:
            return True
    if len(hs) == 10:
        return False
    else:
        return True


def new_record(score, name):
    hs = get_highscore()
    inserted = False
    for i in range(0, len(hs)):
        if score > hs[i][1]:
            hs.insert(i, (name, score))
            hs = hs[0:10]
            inserted = True
            break
        elif score == hs[i][1] and i < 9:
            hs.insert(i + 1, (name, score))
            hs = hs[0:10]
            inserted = True
            break
    if not inserted:
        hs.append((name, score))
    write_highscore(hs)
