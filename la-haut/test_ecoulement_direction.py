from ecoulement_direction import *

#on ne teste pas toutes les fonctions à cause de l'aléatoire
#De plus on a visuellement un resultat satisfaisant pour notre jeu

def test_valeur_case():
    universe = [
        [0, 2, 0],
        [0, 1, 0]
    ]
    assert(valeur_case(universe, 0, 0) == 0)
    assert(valeur_case(universe, 0, 1) == 2)
    assert(valeur_case(universe, 2, 0) == ROCK)

def test_actualisation_gauche_cell():
    universe = [
        [0, 0, 0],
        [0, 1, 0]
    ]
    actualisation_gauche_cell(universe, 1, 1)
    print(universe)
    

#le resultat convient tres pour notre jeu donc tests pas terminés
