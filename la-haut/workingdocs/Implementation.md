<h1>Implementation</h1>

<h2>Représentation de la zone de jeu</h2>

Nous avons appellé "univers" la zone de jeu (là où l'eau coule sur différents materiaux).L'univers est représenté par une matrice d'entiers qui représentent chacun un materiau.  Dans const.py, on trouve les correspondances entiers/materiaux, des fonctions pour reconnaître ces materiaux et des constantes diverses.

<h2>Actualisation de l'univers</h2>

Le jeu est caractérisé par un objet de la classe Niveau, définie dans le fichier niveau.py. L'univers est un attribut de Niveau. Pour l'actualiser d'une génération, il faut appeller la fonction "generation" du fichier fonction_generation.py, qui actualise l'univers.

<h3>Ecoulement de l'eau</h3>

L'écoulement de l'eau est codé dans ecoulement_random.py
Pour actualiser l'écoulement de l'eau il y a trois étapes:

Faire couler chaque particule d'eau qui a de la place en dessous d'elle vers le bas en commançant par faire couler l'eau la plus basse et en actualisant l'univers au fur et à mesure. 

Faire couler l'eau à droite en parcourant l'univers et en choisissant aléatoirement les particules qui se déplacent vers la droite parmi celle qui celles qui sont posées sur un autre bloc. L'ordre d'actualisation de l'univers est important pour que l'écoulement soit réaliste.

Une fois l'univers completement actualisé, on fait de même pour l'écoulement à gauche

Ces deux dernières étapes peuvent être répétée CONST_ECOULEMENT fois, pour différents types d'écoulements

Une modelisation différente de l'ecoulement a été essayée dans ecoulement_direction.py. Ici chaque particule a une direction favorite d'écoulement tant qu'elle n'a pas rencontré pas d'obstacle.

<h3>Source et drain</h3>

Les fonctions associées sont dans source_drain.py

Une source est représentée par un certain bloc (voir dans const.py) elle fait couler de l'eau en dessous d'elle à chaque génération et coule pendant un  temps de niveau.duree_source (niveau.py)

Le drain est un tuyau qui incrémente "niveau.compteur" et absorbe de l'eau lorsque qu'elle tombe dessus. Son fonctionnement est inclu dans la fonction actualisation_bas_cell du fichier ecoulement_random.py

<h3>Options diverses</h3>

<h5> Plantes </h5>

Les plantes sont implémentées dans plante.py. Il s'agit d'un bloc qui lorsqu'il touche de l'eau la remplace par un bloc de plante avec la probabilité PROBA_PLANTE et par du vide sinon. 

<h5>Dynamite</h5>

Les dynamites sont implémentées dans dynamite.py. Une dynamite est représenté par un bloc central qui explose sur un certain rayon, détruisant les blocs sur son passage. Pour l'animation d'explosion de la dynamite, il faut savoir depuis combien de génération elle est sur l'univers et et le rayon d'explosion désiré. Ces informations sont pour l'instant codées de manière pas très propre dans l'entier qui représente le bloc central de la dynamite. Cela serait mieux d'utiliser pour cela une liste des dynamites avec toutes les informations nécessaires et leurs coordonnée dans un attribut de la classe Niveau.

<h2>Génération automatique de niveau</h2>

 Ce type de niveau est généré aléatoirement à l'aide de la règle de la majorité. Au départ, des blocs ROCK_PERMANENT sont posés aléatoirement dans un univers vide avec une probabilité donnée, puis la règle de majorité crée une map aléatoire, où la drain (l'arrivée) et la source le sont aussi. La règle de la majorité est un automate cellulaire qui consiste à attribuer à une case la valeur de la majorité des cases aux alentours. Ceci est implémenté dans generate_obstacles_aléatoires

<h2>Interface graphique avec pygame</h2>

<h3>Affichage de l'univers</h3>

<h3>Interface interactive pour le joueur</h3>
