from generate_universe import *
import os
from pathlib import PurePath, Path
import math
import pygame.locals
import pygame
from ecoulement_direction import *
import numpy as np
import random as rd
from const import *
import sys
np.set_printoptions(threshold=sys.maxsize)


def univers_aleatoire(size):
    universe = np.zeros(size, dtype=int)
    height = len(universe)
    length = len(universe[0])
    for i in range(height):
        for j in range(length):
            var = rd.random()
            if var > 0.465:
                universe[i][j] = EMPTY
            else:
                universe[i][j] = ROCK_PERMANENT
    return universe


def coordonate(universe, i, j):
    height = len(universe)
    assert height > 0
    length = len(universe[0])
    return (i % height, j % length)


def survival(point, universe):
    (i, j) = point
    etat_cellule = universe[i][j]
    liste_coord = [(i - 1, j - 1), (i - 1, j + 0), (i - 1, j + 1),
                   (i + 0, j - 1),                 (i + 0, j + 1),
                   (i + 1, j - 1), (i + 1, j + 0), (i + 1, j + 1)]
    nbre_cellules_vivantes_voisines = 0
    for pointe in (coordonate(universe, i, j) for i, j in liste_coord):
        # état vivant ou mort des cellules voisines
        if universe[pointe[0]][pointe[1]] == ROCK_PERMANENT:
            nbre_cellules_vivantes_voisines += 1
    if etat_cellule == EMPTY:
        if nbre_cellules_vivantes_voisines > 4:
            return ROCK_PERMANENT
        return EMPTY
    elif etat_cellule == ROCK_PERMANENT:
        if nbre_cellules_vivantes_voisines >= 4:
            return ROCK_PERMANENT
        return EMPTY
    else:
        return etat_cellule


def generation_old(univers):
    '''Prends un univers et le modifie en place pour contenir la generation suivante. Celui-ci est aussi renvoyé'''
    l, L = len(univers), len(univers[0])
    univers_apres = np.zeros((l, L), dtype=int)  # univers à l'instant t+1
    for i in range(l):
        for j in range(L):
            # regarde si la case sera vivante à l'instant t+1
            univers_apres[i][j] = survival((i, j), univers)
    for i in range(l):
        for j in range(L):
            # Pour une modification en place
            univers[i][j] = univers_apres[i][j]
    return univers  # renvoie le nouvel univers


def game_simulate(univers, n):  # nombre diteration
    '''Prends un univers de départ et simule n géneration desssus (donc en place), et le renvoie'''
    for i in range(n):
        univers = generation_old(univers)
    add_drain_to_universe(univers, coord="random")
    add_source_to_universe(univers, coord="random")
    return univers


def block_aleatoires(size):
    return game_simulate(univers_aleatoire(size), 25)


def print_matrice(matrix):
    print("[")
    for row in matrix:
        print(f"[{','.join(map(str, row))}]")
    print("]")
