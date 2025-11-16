from generate_universe import *
from source_drain import *
import random as rd
from const import *
import copy


def direction_eau(val_eau):
    """renvoie -1 si l'eau de valeur val_eau va a gauche, 1 si elle va a droite"""
    proba_droite = 0.5
    if val_eau == R_WATER:
        proba_droite = PROBA_EAU_COTE
    elif val_eau == L_WATER:
        proba_droite = PROBA_EAU_COTE
    proba_droite = 0.5
    x = rd.random()  # renvoie flottant entre 0 et 1
    if x < proba_droite:
        return 1
    else:
        return -1


def actualisation_gauche_cell(universe, i, j):
    "actualise une particule d'eau si elle va aller a gauche"
    if est_case_eau(universe, i, j) and direction_eau(universe[i][j]) == -1 and not (est_case_vide(universe, i + 1, j)):
        if est_case_vide(universe, i, j - 1):
            universe[i][j - 1] = WATER
            universe[i][j] = EMPTY
        else:
            universe[i][j] = WATER


def actualisation_droite_cell(universe, i, j):
    "actualise une particule d'eau si elle va aller a droite"
    if est_case_eau(universe, i, j) and direction_eau(universe[i][j]) == 1 and not (est_case_vide(universe, i + 1, j)):
        if est_case_vide(universe, i, j + 1):
            universe[i][j + 1] = WATER
            universe[i][j] = EMPTY
        else:
            universe[i][j] = WATER


def actualisation_bas_cell(universe, i, j, niveau):
    """code la chute verticale des particules d'eau (si elle tombe dans le fond du tuyau incremente le compteur (un pointeur) et disparaissent)"""
    # si la particule peut tomber elle tombe
    if est_case_eau(universe, i, j) and est_case_vide(universe, i + 1, j):
        universe[i+1][j] = universe[i][j]
        universe[i][j] = EMPTY
    # si elle rentre dans le tuyau elle disparait
    if est_case_eau(universe, i, j) and est_case_fond_drain(universe, i+1, j):
        universe[i][j] = EMPTY
        niveau.compteur = niveau.compteur + 1


def generation_gauche(universe):
    "actualise que les particules d'eau qui vont aller a gauche"
    n_x = len(universe)
    n_y = len(universe[0])
    for i in range(n_x):
        for j in range(n_y):
            actualisation_gauche_cell(universe, i, j)


def generation_droite(universe):
    "actualise que les particules d'eau qui vont aller a droite"
    n_x = len(universe)
    n_y = len(universe[0])
    for i in range(n_x):
        for j in range(n_y - 1, -1, -1):
            actualisation_droite_cell(universe, i, j)
