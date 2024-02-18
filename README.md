G E O Q U I Z 

********* COMMENT JOUER ??? ***********************************************************

Pour lancer le programme du jeu, il suffit de lancer main.py, les règles précises sont ensuite expliquées en cliquant sur le bouton "règles" du menu.

/!\ En multijoueur, il est recommandé de désactiver le pare-feu "réseau avec domaine" (ou "réseau privé" si cela ne fonctionne pas)

********* CLIENT SERVEUR ***********************************************************

- Il est possible de jouer en multijoueur local en hébergeant un serveur et en rejoigant la partie grace à l'ip de serveur
- Le serveur va essayer de trouver de nouveaux clients en boucle en multi-threading
- Dès qu'un nouveau client arrive, il démarre un nouveau thread et envoi l'information à tout les autres clients
- Toutes les secondes, le serveur envoie un message à tout les clients, si aucun message doit être envoyé, alors il envoie "en attente"
- Si le serveur lance la partie, il envoie "lancement partie" ainsi qu'une seed qui sera la même pour tout les clients (pour que tout le monde joue avec les mêmes questions)
- Si un joueur se déconnecte, il envoie l'information au serveur, qui l'enlève de la liste et ferme son thread puis envoie l'information à tout les autres clients


********* BASE DE DONNEES ***********************************************************

- La base de données est composée d'une seule table, elle meme composée de nombreuses statistiques comme les noms/capitales/superficies...
- Il y a trois types de valeurs :
  				- Des valeurs numériques (superficie, population, perimètre...)
				- Des chaines de caractères (nom, capitale, langue...)
				- Des booléens (possession d'un territoire en antarctique et accès à la mer)
- La colonne 'frontieres' contient les noms de tous les pays frontaliers du pays
- Le programme creation_questions crée un objet 'pays' avec toutes les caractéristiques de la base de données


********* APPARITIONS DES QUESTIONS ***********************************************************

- Les questions fonctionnent grace à 5 listes (correspondant aux 5 questions de la serie)
- Un pays est tiré au sort grâce à une seed générée en amont (pour qu'en multijoueur tout le monde ait les mêmes questions), puis des attributs lui sont attribués au hasard (capitale, frontières ...) et si pour chaque question il y a assez (mais pas trop) de pays la seed est gardée sinon une nouvelle seed est tirée au sort et le programme recommence jusqu'à avoir un pays et des attributs qui correspondent à toutes les conditions
- Chaque liste contient une selection d'attributs afin de ne pas avoir de questions trop précises trop tôt dans le but de trouver un résultat en exactement 5 questions
- Un attribut est tiré au hasard dans chaque liste et chaque attribut séléctionné fait disparaitre ceux du meme type dans les listes suivantes pour ne pas avoir deux questions identiques


********* PROGRAMMES ***********************************************************

- main : le programme principal qu'il faut de lancer (main_fix à cause des nouvelles versions de python)
- creation_questions : le programme qui trouve 1 pays et 5 questions qui répondent à toutes les conditions
- nommer_questions : le programme permet de nommer les questions à partir d'un attribut et de une/plusieurs valeurs (ex : capitale + P donne "L'initiale de la capitale commence par P")
- simplificateur : le programme permet de simplifer des mots et des listes de mots pour éviter les erreurs d'accents et les pays trop compliquées
- multi_client : le programme qui permet de gerer la connexion au serveur, la déconnexion par le client
- multi_serveur : le programme qui crée le serveur et qui gère tout les clients


********* SHEMA EXPLICATIF SIMPLE ***********************************************************

Lancement d'une partie : jouer --> génère une seed --> génère un pays et des attributs --> se répète tant que toutes les conditions ne sont pas réunies --> nomme les questions --> simplifie les réponses possibles --> renvoie au programme les listes (questions, reponses, infos)


********************************************************************

par Léandro, Dionys, Mathieu, Estéban
