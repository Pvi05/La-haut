from generate_universe import *

exemples_d_obstacles={"cube":[[2,2],[2,2]],
                      "marche_gauche":[[0,2],[2,2]],
                      "marche_droite":[[2,0],[2,2]],
                      "longueur":[[2,2,2,2]]}

universe_test = generate_universe((4,2))

def test(universe, obstacle, x_start="random", y_start="random"):
    add_obstacle_to_universe(universe, obstacle, x_start="random", y_start="random")
    return universe_test