def compteur_score(universe, zone):
    nbre_gouttes = 0
    for elt in zone:
        if elt == 1:
            nbre_gouttes += 1
    return nbre_gouttes


def proportion_eau(universe, zone, nbre_total_gouttes):
    nbre_gouttes = compteur_score(universe, zone)
    return nbre_gouttes/nbre_total_gouttes


def compteur_eau_perdue(universe, zone_arrivée, nbre_total_gouttes):
    nbre_gouttes_finalement = compteur_score(universe, zone_arrivée)
    return nbre_total_gouttes - nbre_gouttes_finalement
