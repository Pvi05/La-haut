#Premiere version de l'ecoulement de l'eau qui coule trop à droite et est difficile à lire...

import random as rd



def generation_trop_a_droite(universe):
    l = [-1,1]
    n_x = len(universe)
    n_y = len(universe[0])
    i = n_x - 1 #on se place à la dernière ligne de la matrice
    j = 1
    while j < n_y -1 : #on évite les bords, on les fera après
        deja_traite =False
        if universe[i][j] == 1 : #les 1 représentent l'eau, 2 les obstacles et les 0 le vide
                universe[i][j] = 0 #on met un zéro car on part du principe que ça va bouger
                if universe[i][j-1] == 0 and universe[i][j+1] == 0 : # on regarde si y a rien à droite ou à gauche
                    x = rd.randint(0,1)
                    universe[i][j + l[x]] = 1
                    deja_traite = True
                    if x == 1:
                        j += 1
                elif universe[i][j-1] == 0 and (universe[i][j+1] == 1 or universe[i][j+1] == 2) and (not deja_traite): #on regarde si y a un truc d'un côté
                    universe[i][j-1] = 1
                elif (universe[i][j-1] == 1 or universe[i][j-1] == 2) and universe[i][j+1] == 0 and (not deja_traite) :
                    universe[i][j+1] = 1
                else: #on se rend compte qu'on a pas bougé
                    universe[i][j] = 1
        j += 1
    j = 0 #on s'occupe du bord de gauche
    if universe[i][j] == 1 :
            universe[i][j] = 0    
            if universe[i][j+1] == 0 :
                universe[i][j+1] = 1    
            else:
                universe[i][j] = 1
    j = n_y -1 #on s'occupe du bord de droite
    if universe[i][j] == 1 :
            universe[i][j] = 0    
            if universe[i][j-1] == 0 :
                universe[i][j-1] = 1
            else:
                universe[i][j] = 1
    i -= 1
    while i >= 0 :#on s'occupe du cas général
        j = 1
        while j < n_y - 1 :
            deja_traite = False
            if universe[i][j] == 1 : 
                universe[i][j] = 0   
                if universe[i+1][j] == 0:
                    universe[i+1][j] = 1
                elif universe[i][j-1] == 0 and universe[i][j+1] == 0 : #attention ici on va devoir sauter une étape
                    x = rd.randint(0,1)
                    universe[i][j + l[x]] = 1
                    deja_traite = True
                    if x == 1:
                        j +=1
                elif universe[i][j-1] == 0 and (universe[i][j+1] == 1 or universe[i][j+1] == 2) and (not deja_traite):
                    universe[i][j-1] = 1
                elif (universe[i][j-1] == 1 or universe[i][j-1] == 2) and universe[i][j+1] == 0 and (not deja_traite):
                    universe[i][j+1] = 1
                else:
                    universe[i][j] = 1
            j += 1
        j = 0
        if universe[i][j] == 1 :
            universe[i][j] = 0    
            if universe[i+1][j] == 0:
                universe[i+1][j] = 1
            elif universe[i][j+1] == 0 :
                universe[i][j+1] = 1
            else:
                universe[i][j] = 1
        j = n_y -1 
        if universe[i][j] == 1 :
            universe[i][j] = 0    
            if universe[i+1][j] == 0:
                universe[i+1][j] = 1
            elif universe[i][j-1] == 0 :
                universe[i][j-1] = 1
            else:
                universe[i][j] = 1
        i -= 1