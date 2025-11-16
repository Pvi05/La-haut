<h1>Là Haut: Projet des coding weeks 2024-2025 de la team Con-vie-vial</h1>

<h2>Description</h2>
Le projet est un jeu consistant à guider une chute d'eau entre des obstacles afin d'amener le plus d'eau possible dans un tuyau. Le joueur peut pour cela placer ou effacer certains blocs. Certains niveaux de jeu sont déjà enregistrés mais il est aussi possible de générer des niveaux automatiquement.

Notre projet inclut aussi un module permettant de créer soit même des niveaux de jeu mais celui-ci n'est pas encore disponible depuis le menu principal car pour l'instant reservé au developpement/mod. 

<h2>La team Con-vie-vial</h2>
<li>Membre 1 : Enguerrand de Jaegere </lu>
<li>Membre 2 : Emile L'Excellent</lu>
<li>Membre 3 : Paul VILARS</lu>
<li>Membre 4 : Paul Verhaeghe</lu>
<li>Membre 5 : Maxime lpb </lu>
<li>Membre 6 : Tizianuile </lu>

<h2>Installation</h2>

Avant d'utiliser notre projet, il faudra installer les modules pythons du fichier nommé _requirements.txt_. Vous pouvez les installer avec le module pip. Il faut aussi avoir tous les modules du dossier "la-haut".

<h2>Utilisation</h2>

Pour lancer le jeu, il suffit de lancer le fichier _display_launcher.py_.

Pour créer soi-même des niveaux du jeu il est possible de lancer l'éditeur de niveau en lancant le fichier _level_editor.py_. Il est important de garder en tête que cette fonctionnalité est principalement destinée au devellopement ou au mod pour l'instant. Un descriptif plus poussé de cette fonction est disponible plus bas.

<h2>Jouer une partie</h2>

Après avoir lancé le jeu et cliqué sur **play** vous arriverez sur la fenêtre des niveaux.
Les niveaux numérotés sont déjà implémentés et le niveau **random** est généré automatiquement.

Commencez un niveau en cliquant dessus.
Lors d'une partie, une zone de couleur bleu claire indique la source. C'est de là que l'eau coulera vers le bas dès que la touche **lancer/pause** (touche espace) sera pressée. Après un certain temps, la source finira par être épuisée et donc par ne plus couler. 
Le joueur peut, à tout moment, à l'aide des boutons **draw** et **erase** placer ou enlever des blocks gris. 

Son but est que le plus d'eau possible tombe dans le tuyau (ou _drain_) présent en bas de la fenêtre, et le nombre de gouttes d'eau récoltées est indiquée par le compteur. À partir d'une certaine quantité d'eau récoltée (qui dépend du niveau) la victoire est déclarée.
Le jeu présente aussi différentes mécaniques de jeu commme la présence de d'autres materiaux aux propriétés particulières (plantes par exemple qui absorbent l'eau) ou encore la possibilité de poser de la dynamite (qui détruit l'obsidienne), ajoutant de la difficulté au niveau.
A noter que le joueur dispose d'une quantité limité de dynamite.

Si le joueur ne pense plus pouvoir gagner, il peut appuyer sur **reset** (_aussi touche r_) pour ramener le niveau à l'etat initial. 

Si le joueur souhaite annuler sa dernière action, il peut appuyer sur **cancel** (_aussi touche b_) pour ramener le niveau à son l'etat lors de la dernière pause.

<h2>Fonctions principales</h2>

Notre "univers", la zone dans laquelle évoluent les particules d'eau et les blocs est une matrice que l'on modifie grâce à la fonction generation. Une explication du fonctionnement plus précis est disponible dans Implementation.md

Quelques fonctions on été écrites en TDD avec des fichiers tests au début du projet mais étant donné la part d'aléatoire et puisque nous possédions ensuite une interface, il était bien plus simple de tester nos fonctions directement en utilisant l'interface en testant nous même différents cas dont ceux qui nous semblaient critiques (avec l'inconvénient qu'il nous reste donc peu de traces).

<h2>Support</h2>

Les membres de l'équipe

<h2>Etat du projet</h2>

En cours.
Nous y travaillerons moins régulièrement à partir de la fin des deux semaines de coding weeks(jusqu'au 23 novembre 2024).

<h2>La fonction d'édition de niveau</h2>

**Cette fonction est pour l'instant reservée à un usage de développement et de modding.**

Lancer l'éditeur de niveau ce fait en exécutant le fichier _level_editor.py_.
L'interface est sommaire et comporte deux grandes fonctionnalités :
- Plusieurs boutons afin d'accéder aux textures les plus utilisés
- Une entrée de texte pour choisir un bloc en particulier, à l'aide de son code. L'ensemble des blocs disponibles et leur code (un entier) est accessible dans le fichier _const.py_.
_Par exemple, pour choisir l'obsidienne (bloc sombre cassable uniquement par dynamite), il faut rentrer le code 22 dans l'entrée de texte._

Les boutons sources et drain permettent de placer automatiquement la source et le drain en cliquant sur la position souhaité. Il est aussi possible de les placer manuellement à l'aide des blocs correspondants.

Une fois que le niveau est fini, le bouton export permet d'imprimer le niveau dans un fichier _output.txt_.
Pour le rendre accessible, il faut l'affecter à un niveau dans le dictionnaire _dict_niveau_ (dans _display_in_game.py_).

<h2>Idées pour le futur</h2>

-> Retravailler le fichier level_editor.py pour que son utilisation soit plus simple afin de le rendre accessible à tout utilisateur.

-> Une nouvelle modelisation de l'eau qui s'écoule moins aléatoirement. le fichier ecoulement_direction.py est un essain de particules d'eau qui gardent la même direction (gauche ou droite) jusqu'à rencontrer un obstacle mais les résultats ne sont pas satisfaisant.

-> Des nouveaux matériaux originaux pour rendre les niveaux encore plus épicés!

<h2>Sources d'inspiration</h2>

Les liens suivants nous ont aidés à avancer dans notre projet : 
Pour la modelisation du jeu:
https://youtu.be/dh-s-DAvPkI?si=OkqP3RVm6wZPb-Ln
Pour créer des niveaux automatiquement :
https://courses.cs.ut.ee/2020/cg-pro/spring/Main/Project-AutomataSandbox






