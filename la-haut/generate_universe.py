import numpy as np
import random as rd
from const import *
import math




def generate_universe(size):
    universe = np.zeros(size, dtype=int)
    return universe


def add_obstacle_to_universe_aléatoire(universe, nbre_obstacles):
    H = len(universe)
    L = len(universe[0])
    Coord_obstacles = []
    x, y = (rd.randint(0, H-1), rd.randint(0, L-1))
    Coord_obstacles.append((x, y))
    for _ in range(nbre_obstacles-1):
        while (x, y) in Coord_obstacles:
            x, y = rd.randint(0, H-1), rd.randint(0, L-1)
        Coord_obstacles.append((x, y))
        universe[x][y] = 2


def add_obstacle_to_universe(universe, obstacle, x_start="random", y_start="random"):
    assert ((len(obstacle) <= len(universe)) & (
        len(obstacle[0]) <= len(universe[0])))
    if isinstance(x_start, int) & isinstance(y_start, int):
        x, y = x_start, y_start
    else:
        x, y = rd.randint(0, len(universe) - len(obstacle)
                          ), rd.randint(0, len(universe[0]) - len(obstacle[0]))
    for yi in range(0, len(obstacle)):
        for xi in range(0, len(obstacle[0])):
            xin, yin = xi + x, yi + y
            universe[xin][yin] = obstacle[xi][yi]


def est_dans_lunivers(univers, coord):
    height = len(univers)
    length = len(univers[0])
    if coord[0] < 0 or coord[0] >= height or coord[1] < 0 or coord[1] >= length:
        return False
    return True
