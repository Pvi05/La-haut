from generate_universe import *
import math
import random as rd


def doit_etre_casse(val_cellule):
    return not (est_dynamite(val_cellule) or val_cellule == PVC or val_cellule == FOND_DRAIN or val_cellule == SOURCE)


def valeur_centre_dynamite(rayon):
    """valeur a poser dans une cellule de l'univers pour qu'il devienne le centre d'une dynamite"""
    return 6 + 10 * rayon


def explosion(universe, coord, rayon): 
    for i in range(coord[0]-rayon, coord[0]+rayon+1):
        for j in range(coord[1]-rayon, coord[1]+rayon+1):
            if abs(coord[0]-i) + abs(coord[1]-j) <= rayon and est_dans_lunivers(universe, (i, j)) and doit_etre_casse(universe[i][j]) and (i, j) != coord:
                universe[i][j] = FEU


def retour_a_la_normale(universe, coord, rayon):
    for i in range(coord[0]-rayon, coord[0]+rayon+1):
        for j in range(coord[1]-rayon, coord[1]+rayon+1):
            if abs(coord[0]-i) + abs(coord[1]-j) <= rayon and est_dans_lunivers(universe, (i, j)) and doit_etre_casse(universe[i][j]) and (i, j) != coord:
                universe[i][j] = EMPTY


def infos_dynamite(val_cellule):
    """renvoie le couple (age, rayon) de la dynamite dont le centre est representee par l'entier val_cellule"""
    rayon = (val_cellule//10) % 1000
    age = val_cellule // 10000
    return (age, rayon)


def prend_infos_dynamite(universe, i, j, liste_dynamite):
    if est_dynamite(universe[i][j]):
        infos = infos_dynamite(universe[i][j])
        age = infos[0]
        rayon = infos[1]
        liste_dynamite.append(((i, j), rayon, age))


def generation_dynamite(niveau, liste_dynamite):
    """met a jour le mouvement des dynamite,chaque element de liste_dynamite est de la forme (coord, rayon, age)"""
    universe = niveau.universe
    for dyna in liste_dynamite:
        coord, rayon, age = dyna
        if age == 0:
            if niveau.nb_dynamite==0:
                universe[coord[0]][coord[1]] = 0
            else :
                niveau.nb_dynamite = niveau.nb_dynamite - 1
                universe[coord[0]][coord[1]] += 10000
        elif age > 2 * rayon:
            universe[coord[0]][coord[1]] = 0
        elif age <= rayon:
            explosion(universe, coord, age)
            universe[coord[0]][coord[1]] += 10000
        elif age >= rayon:
            retour_a_la_normale(universe, coord, age - rayon)
            universe[coord[0]][coord[1]] += 10000
