from display_elements import *
from display_in_game import *
import pygame
import pygame.locals
import time

assert pygame.display.get_init()

WIDTH = 500  # Width of screen in pixels
HEIGHT = 500  # Height of screen in pixels


pygame.display.set_caption("Main Menu")
menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
menu_screen.fill(BACKGROUND_MENU)

title = pygame.transform.scale(FONT_TITLE.render(
    "Là - haut", True, WHITE), (200, 75))


play_button_pic = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/play_button.png")).convert_alpha()
niv_button_pic = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/niveauButton.png")).convert_alpha()
back_button_pic = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/backButton.png")).convert_alpha()
title_frame = pygame.image.load(
    os.path.join(PATH_TO_FILE, "pictures/long_frame.png")).convert_alpha()
title_frame = pygame.transform.scale(title_frame, (250, 100))
play_button = Button(HEIGHT//2 - 50, WIDTH//2 - 50,
                     100, 100, image=play_button_pic, base_color=BACKGROUND_MENU)


SIDE_BUTTON_NIV = 100
HOR_GAP = 50
VERT_GAP = 20


def buttons_niv():
    grid = []
    for i in range(3):
        for j in range(3):
            grid.append((HOR_GAP + j*(SIDE_BUTTON_NIV + HOR_GAP),
                         VERT_GAP + i*(SIDE_BUTTON_NIV + VERT_GAP)))
    niv_button = []
    for i in range(9):
        x, y = grid[i]
        niv_button.append(
            Button(x, y, SIDE_BUTTON_NIV, SIDE_BUTTON_NIV, "Level " + str(i + 1), font=FONT_NIV,  text_color=WHITE, image=niv_button_pic))
    return niv_button


def in_niveau():
    menu_screen.fill(BACKGROUND_MENU)
    buttons = buttons_niv()
    for but in buttons:
        but.draw(menu_screen)
    back_button = Button(2*HOR_GAP, VERT_GAP + 3*(SIDE_BUTTON_NIV +
                                                  VERT_GAP), SIDE_BUTTON_NIV, SIDE_BUTTON_NIV, image=back_button_pic)
    rdm_button = Button(4*HOR_GAP + SIDE_BUTTON_NIV, VERT_GAP + 3*(SIDE_BUTTON_NIV +
                                                                   VERT_GAP), SIDE_BUTTON_NIV, SIDE_BUTTON_NIV, "Random", text_color=WHITE,  image=niv_button_pic)
    rdm_button.draw(menu_screen)
    back_button.draw(menu_screen)
    pygame.display.set_caption("Choose a Level")
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                terminate_app()
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if buttons[0].is_clicked():
                    return 0
                if buttons[1].is_clicked():
                    return 1
                if buttons[2].is_clicked():
                    return 2
                if buttons[3].is_clicked():
                    return 3
                if buttons[4].is_clicked():
                    return 4
                if buttons[5].is_clicked():
                    return 5
                if buttons[6].is_clicked():
                    return 6
                if buttons[7].is_clicked():
                    return 7
                if buttons[8].is_clicked():
                    return 8
                if back_button.is_clicked():
                    return -1
                if rdm_button.is_clicked():
                    return -2


def main():
    global menu_screen
    run = True
    while run:
        menu_screen.fill(BACKGROUND_MENU)
        play_button.draw(menu_screen)
        menu_screen.blit(title_frame, (WIDTH//2 - 100 -
                         25, HEIGHT//4 - 50 - 20 - 10))
        menu_screen.blit(
            title, (WIDTH//2 - 100, HEIGHT//4 - 50 - 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                terminate_app()
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if play_button.is_clicked():
                    niv = in_niveau()
                    if niv == -1:
                        print("back")
                    elif niv == -2:
                        print("random")
                        main_in_game(niv)
                        pygame.display.set_caption("Main Menu")
                        menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    else:
                        print("niveau ", 1)
                        pygame.display.quit()
                        main_in_game(niv)
                        pygame.display.set_caption("Main Menu")
                        menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))


main()
