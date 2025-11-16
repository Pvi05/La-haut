#Constantes de materiaux

EMPTY = 0

WATER = 1
R_WATER = 11 
L_WATER = 21  #eau droite et gauche pour l'eau qui a une direction
 
ROCK = 2 #rock que l'utilisateur peut poser et effacer
PVC = 12 #materiau incassable du tuyau
ROCK_PERMANENT = 22 

FOND_DRAIN = 3   #l'eau diparait et incremente le compteur d'eau en touchant ce materiau
# x est de l'eau ssi x%10 = 1
# x est SOLIDE ssi x%10 = 2

FEU = 4
PLANTE = 5 #absorbe l'eau
DYNAMITE = 6  # (quand on fait modulo 10 un centre dynamite fait 6)
POSE_DYNAMITE = 56 #centre d'une dynamite qui vient d'être posée
SOURCE = 7 #fait couler de l'eau par le bas


#Constantes diverses

HAUTEUR_DRAIN = 3
LARGEUR_DRAIN = 5  # nbre impair svp

LARGEUR_SOURCE = 1  # nbre impair svp

PROBA_PLANTES = 0.25 #proba qu'une plante grandisse quand elle absorbe de l'eau
ABSCISSE_SOURCE = 5
PROBA_EAU_COTE = 0.98 #proba que de l'eau qui doit aller à droite aille vraiment à droite
CONST_ECOULEMENT = 3

#Fonctions utiles

def est_eau(val_cellule):
    """renvoie true ssi l'entier val_cellule represente de l'eau"""
    return val_cellule % 10 == 1


def est_vide(val_cellule):
    """renvoie true ssi l'entier val_cellule represente du vide"""
    return val_cellule == EMPTY


def est_solide(val_cellule):
    """renvoie true ssi l'entier val_cellule represente un solide"""
    return val_cellule % 10 == 2


def est_rock(val_cellule):
    """renvoie true ssi l'entier val_cellule represente un rock"""
    return val_cellule == ROCK


def est_fond_drain(val_cellule):
    """renvoie true ssi l'entier val_cellule represente le fond du tuyau"""
    return val_cellule == FOND_DRAIN


def est_dynamite(val_cellule):
    """renvoie true ssi l'entier val_cellule represente le centre d'une dynamite"""
    return val_cellule % 10 == DYNAMITE



#Pour faire en sorte que l'eau ne sorte pas de notre univers, on crée la fonction suivante pour que l'exterieu de l'univers soit du ROCK

def valeur_case(universe, i, j):
    """prend univers, i, j et renvoie une valeur correspondant au materiau dans cette cellule (Un ROCK si on est en dehors de l'univers)"""
    n_x = len(universe)
    n_y = len(universe[0])
    if (0 <= i and i < n_x) and (0 <= j < n_y):
        return universe[i][j]
    return 1


def est_case_vide(universe, i, j):
    """renvoie true ssi la case univers[i][j] est vide (potentiellement i, j ne sont pas des coord valides, dans ce cas la case est un rock)"""
    return valeur_case(universe, i, j) == EMPTY


def est_case_eau(universe, i, j):
    """renvoie true ssi la case univers[i][j] est de l'eau (potentiellement i, j ne sont pas des coord valides, dans ce cas la case est un rock)"""
    return est_eau(valeur_case(universe, i, j))


def est_case_solide(universe, i, j):
    """renvoie true ssi la case univers[i][j] est solide (potentiellement i, j ne sont pas des coord valides, dans ce cas la case est un rock)"""
    return est_solide(valeur_case(universe, i, j))


def est_case_fond_drain(universe, i, j):
    """renvoie true ssi la case univers[i][j] est le fond du tuyau (potentiellement i, j ne sont pas des coord valides, dans ce cas la case est un rock)"""
    return est_fond_drain(valeur_case(universe, i, j))
