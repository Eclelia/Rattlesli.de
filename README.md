# Rattlesli.de
Un jeu multijoueur combinant les concepts du jeu retro Snake et Slither.io

## 🎯 Contexte & cahier des charges
Développé dans le cadre d'une formation, afin de développer nos compétences en Python et d'apprendre à utiliser une API

## 🎲 Règles du jeu
Chaque joueur incarne un serpent contrôlable qui peut s'orienter dans les 4 directions cardinales: Nord, Sud, Est, Ouest, et qui se déplace automatiquement sans pouvoir s'arrêter.

L'objectif de chaque joueur est d'augmenter sa longueur en consommant de la nourriture qui apparait dans l'arène, mais aussi d'éliminer les autres joueurs de l'arène en les forçant à cogner leur tête contre le corps de son serpent.

Attention car vous bougez automatiquement, il faut donc prévoir ses mouvements ! 

Toutes les minutes, un nouveau lot de nourriture apparait sur la carte. Soyez le premier à la récupérer !
*(la nourriture est consommée automatiquement lorsque la tête du serpent passe sur la même case)*

Attention ! Pour les autres joueurs, c'est VOUS qui êtes l'ennemi !


**_suite en cours de rédaction_**
## 🎮 Use cases
### 🐉 Administrateur
Expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 

### 🐍 Joueur (apprenant)
- J'apparais avec une longueur de 4 (ma tête, deux segments de corps, ma queue)
- Je peux gagner des points en mangeant de la nourriture
- Je peux gagner des points en éliminant un autre joueur
- Si je meurs, chacun de mes segments a 1 chance sur 3 de lâcher de la nourriture
- Je peux connaitre la longueur et la position de la tête d'un joueur adverse n'importe où sur la carte
- Je peux connaitre l'emplacement de toute la nourriture sur la carte
- Si je touche le bord de la carte, le corps d'un joueur ou mon propre corps, je meurs

## 📞 Diagramme de séquence
Expliquer les points suivants
- [ ] les acteurs
- [ ] le déroulé d'une partie en partant des use case
- [ ] les données échangées entre chaque couche
- [ ] les algorithmes
- [ ] les machines
- [ ] les protocoles réseaux

## ✅ Pré-requis 
- pour l'administrateur
Matériel et logiciel requis pour executer votre projet
- pour les apprenants 
Rediriger vers README API

## ⚙️ Installation
Step by step : commandes à executer par l'administrateur, paquets à installer ...

## 🧪 Tests
- définition du plan de test ce qu'on attend quand on fait quoi 
- step by step pour lancer les tests

## 🛣️ Roadmap
Ce qui reste à faire priorisé dans le temps

## 🧑‍💻 Auteur(s)
- DENNETIERE Célia
- GUILLOT Valentin
- LECROISEY Jean-Victor
- MAFILLE Léo

## 🙏 Remerciements
Nous remercions notre professeur Julien Arne pour son travail, sa patience, ainsi que son aide tout le long du développement de ce jeu.

## ⚖️ License
S'appuyer sur https://choosealicense.com/ ou la doc de github
Attention à vérifier la compatibilité de votre licence avec celles des modules utilisés
