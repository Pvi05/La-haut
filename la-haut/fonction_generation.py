from ecoulement_random import *
from dynamite import *
from plantes import *
from ecoulement_direction import *


def generation_bas_source_plante_liste_dynamite(niveau, liste_dynamite):
    """actualise l'eau qui tombe vers le bas et les plantes. Fait couler de l'eau des cellules source.Met les infos sur les dynamites dans listes_dynamite"""
    universe = niveau.universe
    n_x = len(universe)
    n_y = len(universe[0])
    for i in range(n_x-1, -1, -1):
        for j in range(n_y):
            actualisation_bas_cell(universe, i, j, niveau)
            actualisation_plante_cell(universe, (i, j))
            prend_infos_dynamite(universe, i, j, liste_dynamite)
            generation_source(niveau, i, j)


def generation(niveau):
    universe = niveau.universe
    for _ in range(CONST_ECOULEMENT):
        generation_droite(universe)
        generation_gauche(universe)
    liste_dynamite = []
    generation_bas_source_plante_liste_dynamite(niveau, liste_dynamite)
    generation_dynamite(niveau, liste_dynamite)
    niveau.time += 1

def generation_direction(niveau):
    """Actualise l'univers sachant ou est la source"""
    liste_dynamite = []
    universe = niveau.universe
    generation_bas_source_plante_liste_dynamite(niveau, liste_dynamite)
    for i in range(CONST_ECOULEMENT):
        generation_droite_dir(universe)
        generation_gauche_dir(universe)
    generation_dynamite(niveau, liste_dynamite)
    niveau.time += 1
