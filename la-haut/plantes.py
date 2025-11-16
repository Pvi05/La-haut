
from generate_universe import *
import math
import random as rd


def actualisation_plante_cell(universe, coord):
    """actualise pour une cellule de plante la transformation en plante ou absorbtion de l'eau autour"""
    if universe[coord[0]][coord[1]] == PLANTE:
        voisins = []
        for i in range(coord[0]-1, coord[0]+2):
            for j in range(coord[1]-1, coord[1]+2):
                if est_dans_lunivers(universe, (i, j)) and (i, j) != coord and (i == coord[0] or j == coord[1]):
                    voisins.append((i, j))
        for point in voisins:
            if universe[point[0]][point[1]] == WATER:
                alea = rd.random()
                if alea < PROBA_PLANTES:
                    universe[point[0]][point[1]] = PLANTE
                else:
                    universe[point[0]][point[1]] = EMPTY
