import sys
import os
from pathlib import PurePath, Path
from abc import ABC, abstractmethod
import numpy as np
import math
import pygame.locals
import pygame
from const import *
from fonction_generation import *
from generate_universe import *
from generate_obstacles_aleatoires import *
from display_elements import *
from niveaux import *
from ecoulement_direction import *
from source_drain import *


pygame.init()

WIDTH = 100  # Width of screen in blocks
HEIGHT = 50  # Height of screen in blocks
BLOCK_SIZE = 10  # Size of block in pixel
BACKGROUND = pygame.Color(255, 255, 255)
COLOR_BUTTON = pygame.Color(100, 100, 100)
CURSOR_RADIUS = 2

BLACK = pygame.Color(0, 0, 0)

LEVEL_EDITOR = True
FPS = 70

SOURCE = -1
DRAIN = -2

# p = os.path.dirname(os.path.realpath(__file__))
# logo = pygame.image.load(os.path.join(p, "pictures/logo.png"))
# pygame.display.set_icon(logo)
pygame.display.set_caption("Là-haut")
screen = pygame.display.set_mode(
    (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE), 0, 24)  # New 24-bit screen
screen.fill(BACKGROUND)

clock = pygame.time.Clock()


assert pygame.display.get_init

FONT = pygame.font.Font(None, 12)

s_coor = (-1, -1)
d_coor = (-1, -1)

type = ROCK


class ButtonBlock:
    def __init__(self, xb, yb, widthb, heightb, text, font=FONT, base_color=COLOR_BUTTON, hover_color=None, text_color=BLACK):
        x, y = to_coordonate(xb, yb)
        width, height = to_coordonate(widthb, heightb)
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        if hover_color is not None:
            self.hover_color = hover_color
        else:
            self.hover_color = base_color
        self.text_color = text_color
        self.font = font
        self.text = text
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        # Dessine bouton
        if self.is_hovered():
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.base_color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_hovered(self):
        # Vérifier si la souris est au-dessus du bouton
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self):
        # Vérifier si le bouton est cliqué
        return self.is_hovered() and pygame.mouse.get_pressed()[0]


class SizePickerBlock:
    def __init__(self, xb, yb, widthb, heightb):
        x, y = to_coordonate(xb, yb)
        width, height = to_coordonate(widthb, heightb)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rad = height//2
        self.pwidth = width - self.rad*2
        pygame.draw.rect(self.image, COLOR_BUTTON,
                         (self.rad, height//3, 1, height-2*height//3))
        self.p = 0

    def get_size(self):
        return math.floor(self.p * 10)

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse_buttons[0] and self.rect.collidepoint(mouse_pos):
            self.p = (mouse_pos[0] - self.rect.left - self.rad) / self.pwidth
            self.p = (max(0, min(self.p, 1)))

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        center = (self.rect.left + self.rad + self.p *
                  self.pwidth, self.rect.centery)
        pygame.draw.circle(screen, COLOR_BUTTON,
                           center, self.rect.height // 2)


COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


class InputBox:
    def __init__(self, xb, yb, wb, hb, text=''):
        x, y = to_coordonate(xb, yb)
        w, h = to_coordonate(wb, hb)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global type
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if True:  # int(self.text) in list(color_dict.keys()):
                        print("switched to ", self.text)
                        type = int(self.text)
                        self.text = ""
                    else:
                        print("not an element")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    print(self.text)
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Reset text display
        pygame.draw.rect(screen, BACKGROUND, self.rect, 0)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


buttons = {
    "draw_button": ButtonBlock(1, 1, 5, 2, "draw"),
    "erase_button": ButtonBlock(7, 1, 5, 2, "erase"),
    # "drain": Button(WIDTH/2 - 1, HEIGHT - 3, 2, 2, "")
}

if LEVEL_EDITOR:
    buttons["water_button"] = ButtonBlock(13, 1, 5, 2, "water")
    buttons["place_drain"] = ButtonBlock(19, 1, 5, 2, "drain")
    buttons["place_source"] = ButtonBlock(25, 1, 5, 2, "source")
    buttons["export"] = ButtonBlock(31, 1, 5, 2, "export")
    sizePicker = SizePickerBlock(37, 1, 10, 2)
    sizePicker.draw(screen)
    blockSelect = InputBox(48, 1, 5, 2)
    blockSelect.draw(screen)
    np.set_printoptions(threshold=sys.maxsize)


def buttons_init():
    for _, v in buttons.items():
        v.draw(screen)
    if LEVEL_EDITOR:
        sizePicker.draw(screen)
        blockSelect.draw(screen)


def init_display():
    screen.fill(BACKGROUND)
    buttons_init()
    universe = generate_universe((HEIGHT, WIDTH))
    draw_world(universe)
    return universe


def draw_block(universe, x, y, type=None):
    if type != None:
        universe[x][y] = type
    rect = pygame.Rect(y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    # pygame.draw.rect(screen, color_dict[universe[x][y]], rect)
    pygame.draw.rect(screen, color(universe[x][y]), rect)


def display_actualise():
    buttons_init()
    pygame.display.update()


def draw_world(universe):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            draw_block(universe, x, y)
    buttons_init()
    pygame.display.update()


def get_mouse_coor():
    i, j = pygame.mouse.get_pos()
    return (math.floor(j / BLOCK_SIZE), math.floor(i / BLOCK_SIZE))


def reset_universe(universe):
    print("reset")
    l, L = len(universe), len(universe[0])
    for i in range(l):
        for j in range(L):
            universe[i][j] = EMPTY
    draw_world(universe)


def backup_universe(universe, backup):
    l, L = len(universe), len(universe[0])
    for i in range(l):
        for j in range(L):
            # Pour une modification en place
            universe[i][j] = backup[i][j]
    draw_world(universe)


def fill_blocks_in_cursor(universe, pos, type):
    x, y = pos
    size = sizePicker.get_size()
    for i in range(x - (size//2), x + (size//2) + 1):
        for j in range(y - (size//2), y + (size//2) + 1):
            try:
                draw_block(universe, i, j, type)
            except:
                pass
    display_actualise()


def drawing(universe, type):
    global s_coor
    global d_coor
    while True:
        x, y = get_mouse_coor()
        if type >= 0:
            fill_blocks_in_cursor(universe, (x, y), type)
        else:
            if type == SOURCE:
                add_source_to_universe(universe, coord=(x, y))
            else:
                add_drain_to_universe(universe, coord=(x, y))
            draw_world(universe)
        for event in pygame.event.get():
            if event.type == pygame.locals.MOUSEBUTTONUP:
                return


def runner(universe):
    global type
    print("running")
    backup = np.matrix.copy(universe)
    while True:
        niveau = Niveau(universe, 0, 0)
        generation_direction(niveau)
        draw_world(universe)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return False
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                blockSelect.handle_event(event)
                if buttons["draw_button"].is_clicked():
                    print("Draw clicked!")
                    type = ROCK
                elif buttons["erase_button"].is_clicked():
                    print("Erase clicked!")
                    type = EMPTY
                elif buttons["water_button"].is_clicked():
                    print("Water clicked!")
                    type = WATER
                elif buttons["place_source"].is_clicked():
                    print("Placing source")
                    type = SOURCE
                elif buttons["place_drain"].is_clicked():
                    print("Placing drain")
                    type = DRAIN
                elif sizePicker.is_clicked():
                    sizePicker.update()
                    sizePicker.draw(screen)
                else:
                    drawing(universe, type)
                display_actualise()
            if (event.type == pygame.locals.KEYDOWN):
                blockSelect.handle_event(event)
                if (event.key == pygame.locals.K_SPACE and not blockSelect.active):
                    return True
                if (event.key == pygame.locals.K_r and not blockSelect.active):
                    reset_universe(universe)
                if (event.key == pygame.locals.K_b and not blockSelect.active):
                    backup_universe(universe, backup)
                    return True
        clock.tick(FPS)


def print_matrice_mod(matrix, file):
    print("[", file=open(file, 'a'))
    for row in matrix:
        print(f"[{','.join(map(str, row))}],", file=open(file, 'a'))
    print("]", file=open(file, 'a'))


def pausing(universe):
    global type
    print("paused")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return False
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                blockSelect.handle_event(event)
                if buttons["draw_button"].is_clicked():
                    print("Draw clicked!")
                    type = ROCK
                elif buttons["erase_button"].is_clicked():
                    print("Erase clicked!")
                    type = EMPTY
                elif buttons["water_button"].is_clicked():
                    print("Water clicked!")
                    type = WATER
                elif buttons["export"].is_clicked():
                    print("Exporting")
                    print('ouput_niv = Niveau(\n',
                          file=open('output.txt', 'a'))
                    print_matrice_mod(universe, 'output.txt')
                    print('0, 0)\n',
                          file=open('output.txt', 'a'))
                    print(s_coor, ",", d_coor, file=open('output.txt', 'a'))
                elif buttons["place_source"].is_clicked():
                    print("Placing source")
                    type = SOURCE
                elif buttons["place_drain"].is_clicked():
                    print("Placing drain")
                    type = DRAIN
                elif sizePicker.is_clicked():
                    sizePicker.update()
                    sizePicker.draw(screen)
                elif not blockSelect.active:
                    drawing(universe, type)
            if (event.type == pygame.locals.KEYDOWN):
                blockSelect.handle_event(event)
                if (event.key == pygame.locals.K_SPACE and not blockSelect.active):
                    return True
                if (event.key == pygame.locals.K_r and not blockSelect.active):
                    reset_universe(universe)
        display_actualise()


def main():
    universe = init_display()
    running = True
    while running:
        running = pausing(universe)
        if not (running):
            break
        running = runner(universe)
        print("out")


if __name__ == '__main__':
    main()
