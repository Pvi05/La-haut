
from ecoulement_random import *


# On cherche maintenant a faire de l'eau "DIRECTION" sur le modele de la video youtube dans les sources du readme.md
# Pour cela on ne peut plus faire de modification en place (Cela causait des problèmes d'empilements de particules d'eau)
# il faut donc reecrire la plus part des fonctions


def actualise_ligne(univers, univers_apres, ligne_i):
    """copie la ligne "ligne" de univers_apres dans univers"""
    for j in range(len(univers[0])):
        univers[ligne_i][j] = univers_apres[ligne_i][j]


def actualisation_gauche_cell_dir(universe, universe_apres, i, j):
    "actualise une particule qui va aller a gauche dans univers_apres"
    if est_case_eau(universe, i, j) and direction_eau(universe[i][j]) == -1 and not (est_case_vide(universe, i + 1, j)):
        if est_case_vide(universe, i, j - 1):
            universe_apres[i][j - 1] = L_WATER
            universe_apres[i][j] = EMPTY
        else:
            universe_apres[i][j] = R_WATER


def actualisation_droite_cell_dir(universe, universe_apres, i, j):
    "actualise une particule qui va aller a droite dans univers_apres"
    if est_case_eau(universe, i, j) and direction_eau(universe[i][j]) == 1 and not (est_case_vide(universe, i + 1, j)):
        if est_case_vide(universe, i, j + 1):
            universe_apres[i][j + 1] = R_WATER
            universe_apres[i][j] = EMPTY
        else:
            universe_apres[i][j] = L_WATER


def generation_gauche_dir(universe):
    """actualise toutes  les particules qui vont aller à gauche"""
    n_x = len(universe)
    n_y = len(universe[0])
    universe_apres = copy.deepcopy(universe)
    for i in range(n_x - 1, -1, -1):
        for j in range(n_y):
            actualisation_gauche_cell_dir(universe, universe_apres, i, j)
        actualise_ligne(universe, universe_apres, i)


def generation_droite_dir(universe):
    """actualise toutes  les particules qui vont aller à gauche"""
    n_x = len(universe)
    n_y = len(universe[0])
    universe_apres = copy.deepcopy(universe)
    for i in range(n_x - 1, -1, -1):
        for j in range(n_y - 1, -1, -1):
            actualisation_droite_cell_dir(universe, universe_apres, i, j)
        actualise_ligne(universe, universe_apres, i)
