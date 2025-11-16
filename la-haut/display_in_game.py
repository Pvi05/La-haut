from generate_universe import *
from fonction_generation import *
from const import *
from niveaux import *
from display_elements import *
import pygame
import pygame.locals
import math
import numpy as np
from abc import ABC, abstractmethod
from pathlib import PurePath, Path
import sys

HEIGHT = 50
WIDTH = 100

FPS = 30

# p = os.path.dirname(os.path.realpath(__file__))
# logo = pygame.image.load(os.path.join(p, "pictures/logo.png"))
# pygame.display.set_icon(logo)

SCREEN = None
CLOCK = None

GAME_BUTTON_W = 10
GAME_BUTTON_H = 4

VICTORY = False

button_pic = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/long_frame.png"))
pointer_pic = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/Pointer.png"))

buttons = {
    "draw_button": Button(BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "draw", text_color=WHITE, image=button_pic),
    "dyn_button": Button((2 + GAME_BUTTON_W)*BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "dyn", text_color=WHITE, image=button_pic),
    "erase_button": Button((3 + 2*GAME_BUTTON_W)*BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "erase", text_color=WHITE, image=button_pic),
    "menu_button": Button(WIDTH*BLOCK_SIZE-(GAME_BUTTON_W + 1)*BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "menu", text_color=WHITE, image=button_pic),
    "reset_button": Button(WIDTH*BLOCK_SIZE-(2*GAME_BUTTON_W + 2)*BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "reset", text_color=WHITE, image=button_pic),
    "backup_button": Button(WIDTH*BLOCK_SIZE-(3*GAME_BUTTON_W + 3)*BLOCK_SIZE, BLOCK_SIZE, GAME_BUTTON_W*BLOCK_SIZE, GAME_BUTTON_H*BLOCK_SIZE, "cancel", text_color=WHITE, image=button_pic),
}

sizePicker = SizePicker((5 + 3*GAME_BUTTON_W),
                        1, GAME_BUTTON_W*2, GAME_BUTTON_H, pointer_pic)
dict_niveau = {0: tuto, 1: niveau_2, 2: niveau_3, 3: niveau4, 4: niveau_5, 5:niveau_6, 6:niveau_7, 7:niveau8 }


def UI_init(niveau):
    buttons["dyn_button"].text = f"dynamite : {niveau.nb_dynamite}"
    for _, v in buttons.items():
        v.draw(SCREEN)
    sizePicker.draw(SCREEN)
    score_text = pygame.transform.scale(FONT_TITLE.render(
        f" {niveau.compteur}/{niveau.goal} ", True, BLACK), (7*BLOCK_SIZE, 3*BLOCK_SIZE))
    score_rect = pygame.Rect(WIDTH*BLOCK_SIZE-(4*GAME_BUTTON_W + 4)*BLOCK_SIZE,
                             2*BLOCK_SIZE, 7*BLOCK_SIZE, 3*BLOCK_SIZE)
    pygame.draw.rect(SCREEN, WHITE, score_rect)
    SCREEN.blit(score_text, score_rect)
    if VICTORY:
        vic_text = pygame.transform.scale(FONT_TITLE.render(
            " VICTORY !", True, BLACK), (30*BLOCK_SIZE, 10*BLOCK_SIZE))
        vic_rect = pygame.Rect((WIDTH//2 - 15)*BLOCK_SIZE,
                               (HEIGHT//2 - 5)*BLOCK_SIZE, 30*BLOCK_SIZE, 10*BLOCK_SIZE)
        pygame.draw.rect(SCREEN, WHITE, vic_rect)
        SCREEN.blit(vic_text, vic_rect)


def init_game(niv_int):
    global SCREEN
    global CLOCK
    global HEIGHT
    global WIDTH
    if niv_int == -2:
        niveau = generate_random_niv()
        dict_niveau[-2] = copy_niveau(niveau)
    else:
        try:
            niveau = copy_niveau(dict_niveau[niv_int])
        except:
            niveau = copy_niveau(NIV_VIDE)
    HEIGHT = niveau.height
    WIDTH = niveau.width
    universe = niveau.universe
    pygame.display.init()
    pygame.display.set_caption("Niveau "+str(niv_int + 1))
    SCREEN = pygame.display.set_mode(
        (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE), 0, 24)  # New 24-bit screen
    SCREEN.fill(BACKGROUND)
    CLOCK = pygame.time.Clock()
    assert pygame.display.get_init
    UI_init(niveau)
    draw_world(niveau)
    return niveau


def draw_block(universe, x, y, type=None):
    if type != None and (universe[x][y] == ROCK or universe[x][y] == EMPTY or universe[x][y] == POSE_DYNAMITE):
        universe[x][y] = type
    rect = pygame.Rect(y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    # pygame.draw.rect(SCREEN, color_dict[universe[x][y]], rect)
    pygame.draw.rect(SCREEN, color(universe[x][y]), rect)


def display_actualise(niveau):
    UI_init(niveau)
    pygame.display.update()


def draw_world(niveau):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            draw_block(niveau.universe, x, y)
    UI_init(niveau)
    pygame.display.update()


def get_mouse_coor():
    i, j = pygame.mouse.get_pos()
    return (math.floor(j / BLOCK_SIZE), math.floor(i / BLOCK_SIZE))


def reset_niveau(niveau, niv_int):
    global VICTORY
    print("reset")
    l, L = niveau.height, niveau.width
    niv_or = dict_niveau[niv_int]
    for i in range(l):
        for j in range(L):
            # Pour une modification en place
            niveau.universe[i][j] = niv_or.universe[i][j]
    niveau.compteur = 0
    niveau.time = 0
    niveau.nb_dynamite = dict_niveau[niv_int].nb_dynamite
    VICTORY = False
    draw_world(niveau)


def copy_niveau(niveau):
    new_univ = np.matrix.copy(niveau.universe)
    new_niv = Niveau(new_univ, niveau.nb_dynamite,
                     niveau.goal, niveau.source, niveau.drain)
    return new_niv


def backup_niveau(niveau, niv_backup):
    print("backup")
    l, L = niveau.height, niveau.width
    for i in range(l):
        for j in range(L):
            # Pour une modification en place
            niveau.universe[i][j] = niv_backup.universe[i][j]
    niveau.compteur = niv_backup.compteur
    niveau.time = niv_backup.time
    niveau.nb_dynamite = niv_backup.nb_dynamite
    draw_world(niveau)


def fill_blocks_in_cursor(niveau, pos, type):
    x, y = pos
    size = sizePicker.get_size()
    for i in range(x - (size//2), x + (size//2) + 1):
        for j in range(y - (size//2), y + (size//2) + 1):
            try:
                draw_block(niveau.universe, i, j, type)
            except:
                pass
    display_actualise(niveau)


def drawing(niveau, type):
    while True:
        x, y = get_mouse_coor()
        fill_blocks_in_cursor(niveau, (x, y), type)
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONUP:
                return


def draw_trans_block_on_cursor(niveau, type_g):
    x, y = get_mouse_coor()
    size = sizePicker.get_size()
    if x >= 0 and x < HEIGHT and y >= 0 and y < WIDTH:
        for i in range(x - (size//2), x + (size//2) + 1):
            for j in range(y - (size//2), y + (size//2) + 1):
                try:
                    if (niveau.universe[i][j] == ROCK or niveau.universe[i][j] == EMPTY):
                        # rect = pygame.Rect(j * BLOCK_SIZE, i *
                        #                    BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        # col = color(type_g[0])
                        # col.a = 50
                        # pygame.draw.rect(SCREEN, col, rect)
                        s = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
                        s.set_alpha(128)
                        s.fill(color(type_g[0]))
                        SCREEN.blit(s, (j * BLOCK_SIZE, i * BLOCK_SIZE))
                except:
                    pass
    display_actualise(niveau)


def event_handling(type_g, niveau, paused):
    global VICTORY
    for event in pygame.event.get():
        if niveau.nb_dynamite <= 0 and type_g[0] == POSE_DYNAMITE:
            type_g[0] = EMPTY
        if event.type == pygame.locals.QUIT:
            terminate_app()
        if (event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE):
            return True
        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            if buttons["draw_button"].is_clicked():
                print("Draw clicked!")
                type_g[0] = ROCK
            elif buttons["erase_button"].is_clicked():
                print("Erase clicked!")
                type_g[0] = EMPTY
            elif buttons["menu_button"].is_clicked():
                print("Back to menu")
                return False
            elif buttons["dyn_button"].is_clicked():
                print(niveau.nb_dynamite)
                if niveau.nb_dynamite > 0:
                    type_g[0] = POSE_DYNAMITE
                else:
                    print("test ?")
                    type_g[0] = EMPTY
            elif buttons["backup_button"].is_clicked():
                return "backup"
            elif buttons["reset_button"].is_clicked():
                raise Reset
            elif sizePicker.is_clicked():
                sizePicker.update()
                sizePicker.draw(SCREEN)
            else:
                drawing(niveau, type_g[0])
            display_actualise(niveau)
        if (event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_r):
            raise Reset
        if (event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_b):
            return "backup"
    if niveau.compteur > niveau.goal:
        VICTORY = True


def runner(type_g, niveau):
    print("running")
    backup = copy_niveau(niveau)
    while True:
        generation(niveau)
        draw_world(niveau)
        response = event_handling(type_g, niveau, False)
        if response == "backup":
            backup_niveau(niveau, backup)
            return True
        if isinstance(response, bool):
            return response
        draw_trans_block_on_cursor(niveau, type_g)
        CLOCK.tick(FPS)


def pausing(type_g, niveau):
    print("paused")
    while True:
        draw_world(niveau)
        response = event_handling(type_g, niveau, True)
        if isinstance(response, bool):
            return response
        draw_trans_block_on_cursor(niveau, type_g)
        CLOCK.tick(FPS)


def main_in_game(niv_int):
    global VICTORY
    VICTORY = False
    niveau = init_game(niv_int)
    running = True
    type_drawing = [ROCK]
    while running:
        print(VICTORY)
        try:
            running = pausing(type_drawing, niveau)
            if not (running):
                break
            running = runner(type_drawing, niveau)
            print("out")
        except Reset:
            reset_niveau(niveau, niv_int)
