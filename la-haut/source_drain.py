from generate_universe import *

# attention ici le start_point est la case de gauche donc attention à ne pas dépasser


def place_source(largeur, start_point, universe):
    """place une source dans l'univers"""
    n_y = len(universe[0])
    y = start_point[1]
    x = start_point[0]
    if largeur + y >= n_y:
        for j in range(y, n_y - 1):
            if universe[x][j] == EMPTY:
                universe[x][j] = SOURCE
    else:
        for j in range(y, y+largeur):
            if universe[x][j] == EMPTY:
                universe[x][j] = SOURCE


def generation_source(niveau, i, j):
    universe = niveau.universe
    if universe[i][j] == SOURCE and niveau.time < int(niveau.duree_source):
        universe[i + 1][j] = WATER


def coord_drain(universe):
    height = len(universe)
    length = len(universe[0])
    valid = False
    while not valid:
        i, j = rd.randint(height-5, height-3), rd.randint(3, length-3)
        if universe[i][j] == 0:
            valid = True
    return (i, j)


def add_drain_to_universe(universe, coord="random"):
    height = HAUTEUR_DRAIN
    length = LARGEUR_DRAIN
    part_ent1 = math.floor(height/2)
    part_ent2 = math.floor(length/2)
    drain = np.zeros((height, length), dtype=int)
    for i in range(height):
        for j in range(length):
            if i == height-1:
                drain[i][j] = FOND_DRAIN
            else:
                if j == 0 or j == (length - 1):
                    drain[i][j] = PVC
    vraies_coord = coord_drain(universe)
    if not (isinstance(coord, str)):
        vraies_coord = coord
    i, j = vraies_coord[0], vraies_coord[1]
    for k in range(-part_ent1, part_ent1 + 1):
        for p in range(-part_ent2, part_ent2 + 1):
            universe[i+k][j+p] = int(drain[part_ent1+k][part_ent2+p])


def coord_source(universe):
    height = len(universe)
    length = len(universe[0])
    valid = False
    while not valid:
        i, j = rd.randint(0, 3), rd.randint(1, length-3)
        if universe[i][j] == 0:
            valid = True
    return (i, j)


def add_source_to_universe(universe, coord="random"):
    length = LARGEUR_SOURCE
    part_ent2 = math.floor(length/2)
    source = np.zeros((1, length), dtype=int)
    for j in range(length):
        source[0][j] = SOURCE
    if isinstance(coord, str):
        coord = coord_source(universe)
        i = ABSCISSE_SOURCE
    else:
        i = coord[0]
    j = coord[1]
    for p in range(-part_ent2, part_ent2 + 1):
        universe[i][j+p] = int(source[0][part_ent2+p])
