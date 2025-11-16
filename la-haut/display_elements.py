import pygame
import math
import os
import sys
from const import *
pygame.init()

PATH_TO_FILE = os.path.dirname(os.path.realpath(__file__))

FONT = pygame.font.Font(os.path.join(PATH_TO_FILE, "font/p_font.ttf"), 12)
BLOCK_SIZE = 10  # Size of block in pixel
BACKGROUND = pygame.Color(255, 255, 255)
COLOR_BUTTON = pygame.Color((45, 48, 61))
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BACKGROUND_MENU = pygame.Color((45, 48, 61))
FONT_TITLE = pygame.font.Font(os.path.join(
    PATH_TO_FILE, "font/p_font.ttf"), 100)
FONT_NIV = pygame.font.Font(os.path.join(
    PATH_TO_FILE, "font/p_font.ttf"), 15)


color_dict = {
    WATER: pygame.Color(43, 155, 209),
    EMPTY: BACKGROUND,
    ROCK: pygame.Color(124, 127, 122),
    R_WATER: pygame.Color(43, 155, 209),
    L_WATER: pygame.Color(43, 155, 209),
    PVC: pygame.Color(46, 0, 108),
    PLANTE: pygame.Color(20, 148, 20),
    FOND_DRAIN: pygame.Color(187, 210, 225),
    FEU: pygame.Color(247, 35, 12),
    ROCK_PERMANENT: pygame.Color((32, 26, 47)),
    DYNAMITE: pygame.Color(0, 0, 0),
    SOURCE: pygame.Color(37, 253, 233)
}

# HOP JE RAJOUTE


def color(val_cellule):
    if val_cellule in color_dict:
        return color_dict[val_cellule]
    if est_dynamite(val_cellule):
        return color_dict[DYNAMITE]


def to_coordonate(xblocks, yblocks):
    return xblocks * BLOCK_SIZE, yblocks * BLOCK_SIZE


def terminate_app():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


class Reset(Exception):
    pass


class Button:
    def __init__(self, x, y, width, height, text="", font=FONT, base_color=COLOR_BUTTON, hover_color=None, text_color=BLACK, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        if hover_color is not None:
            self.hover_color = hover_color
        else:
            self.hover_color = base_color
        if image is not None:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.image = None
        self.text_color = text_color
        self.font = font
        self.text = text
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(
            center=self.rect.center)

    def draw(self, screen):
        # Dessine bouton
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(
            center=self.rect.center)
        if self.image is None:
            if self.is_hovered():
                pygame.draw.rect(screen, self.hover_color, self.rect)
            else:
                pygame.draw.rect(screen, self.base_color, self.rect)
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_hovered(self):
        # Vérifier si la souris est au-dessus du bouton
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self):
        # Vérifier si le bouton est cliqué
        return self.is_hovered() and pygame.mouse.get_pressed()[0]


class SizePicker:
    def __init__(self, xb, yb, widthb, heightb, p_pic=None):
        x, y = to_coordonate(xb, yb)
        width, height = to_coordonate(widthb, heightb)
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rad = height//2
        self.pwidth = width - self.rad*2
        pygame.draw.rect(self.image, COLOR_BUTTON,
                         (self.rad, height//3, width-2*self.rad, height-2*height//3))
        if p_pic is not None:
            self.pic = pygame.transform.scale(p_pic, (height, height))
        else:
            self.pic = None
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
        if self.pic is None:
            pygame.draw.circle(screen, COLOR_BUTTON,
                               center, self.rect.height // 2)
        else:
            _, height = self.rect.size
            x, y = self.rect.x, self.rect.y
            rect_p = pygame.Rect(center[0] - height//2, y, height, height)
            screen.blit(self.pic, rect_p)
