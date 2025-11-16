from generate_universe import *
from ecoulement_eau import *


#test validé ok
def test_actualisation_grille():
    univers = np.array([
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=np.uint8)
    univers_correct_1 = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    univers_correct_2 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    generation(univers)
    print(univers)
    test_equality_1 = np.array(univers == np.array(univers_correct_1, dtype=np.uint8))
    test_equality_2 = np.array(univers == np.array(univers_correct_2, dtype=np.uint8))
    assert (test_equality_1.all() or test_equality_2.all())
    univers = np.array([
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]
    ], dtype=np.uint8)
    univers_correct_1 = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0]
    ]
    univers_correct_2 = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [2, 0, 2, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]
    ]
    generation(univers)
    print(univers)
    test_equality_1 = np.array(univers == np.array(univers_correct_1, dtype=np.uint8))
    test_equality_2 = np.array(univers == np.array(univers_correct_2, dtype=np.uint8))
    assert (test_equality_1.all() or test_equality_2.all())

test_actualisation_grille()