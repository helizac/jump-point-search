# Jump Point Search Implementation

Ce repository est une implémentation Python de "Jump Point Search" Algorithme sur le site Web de Flask.

Remarque : Pour ce référentiel, l'algorithme de recherche de point de saut est implémenté dans une version de passage d'angle. Et pris avancer chaque unité coûte 1, avancer les diagonales coûte 2^(1/2).

<br>

<div align="center">
    <img src="https://user-images.githubusercontent.com/54884571/210881047-0e17d0cb-9606-45c3-ade8-9e6bf3408ff9.gif" height="56" border="2"/>
</div>

## Le Contenu

<div>
    <ol>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#project-architecture">Architecture du Projet</a></li>
        <li><a href="jps">Algorithme de JPS Détaillée</a></li>
        <li><a href="#results">Résultats</a></li>
        <li><a href="#conclusion">Conclusion</a></li>
        <li><a href="#references">Références</a></li>
    </ol>
</div>

<h2 id="introduction">Introduction</h2>

L'algorithme de recherche de points de saut est très efficace, en particulier dans les jeux de donjon ou dans les zones comportant de nombreux obstacles. C'est pourquoi j'ai utilisé un thème de donjon sur le site Web. Pour le bien des personnages de champignons qui ont été écrasés pendant des années, un puissant champignon poursuit Mario sur le site Web. Avec l'algorithme JPS, Mario peut s'échapper du champignon.

#### Qu'est-ce que l'algorithme de JPS ( Jump Point Search - Recherche de Point de Saut ) ?

La recherche de points de saut (JPS) est un algorithme de recherche de chemin pour les graphes qui est une optimisation de l'algorithme de recherche A*. Il est conçu pour trouver efficacement un chemin le plus court entre deux points dans un graphique qui a beaucoup plus de chemins possibles que la simple distance en ligne droite entre les deux points. L'algorithme fonctionne en "sautant" sur les nœuds du graphique qui ne sont probablement pas sur le chemin optimal, en utilisant des "points de saut" précalculés pour se rapprocher rapidement de l'objectif. Cela peut réduire considérablement le nombre de nœuds à évaluer, ce qui rend la recherche beaucoup plus rapide qu'une recherche A* standard. JPS est particulièrement bien adapté pour une utilisation dans les graphiques basés sur une grille, tels que ceux utilisés dans de nombreux jeux vidéo et applications robotiques.

<h2 id="project-architecture">Architecture du Projet</h2>

```
- .github
    - workflow
        + static.yml # Pour afficher une page statique dans Github
- web
    - static
        - css
            + style.css # contient un fichier de style pour home.html (a également des animations à l'intérieur)
        - js 
            + grid.js # crée des grilles et gère les événements de grille. Gère également les animations.
            + lottie.js # un fichier d'intégration de loterie simple pour une utilisation facile.
        - lottie
            + animation1.gif
            + fireworks.json
            + mario.gif
            + mushroom.gif
            + paper.json
            + tile.png
    - templates
        + home.html # page principale (envoie également des données au back-end et prend la réponse de la grille après la jump_point_search.py) 
    + __init__.py # gère Flask et les propriétés de configuration
    + routes.py # page de routage Flask de base qui contacte le front-end pour trouver le chemin.
+ .gitattributes
+ .gitignore
+ LICENSE
+ jump_point_search.py # Fichier d'implémentation de la recherche de points de saut
+ main.py # fichier principal pour exécuter tous les codes ci-dessus
+ readme.md
```

Pour ce projet, il n'y a que deux bibliothèques qui doivent être installées dans le terminal. Utilisez pip3 ou pip pour les packages d'installation.

Pour installer simplement les bibliothèques, tapez après avoir ouvert le cmd dans le fichier jump-point-search ->
```
pip install -r requirements.txt
```

et qui s'installera immédiatement ->
```
Flask==2.2.2
numpy==1.23.5
```

Après ce type ->
```
python main.py
```

Et voilà. Un lien s'ouvrira dans votre navigateur. ( Sinon, ctrl+clique sur l'url. )

<h2 id="jps">Algorithme de JPS Détaillée</h2>

L'algorithme commence au nœud de départ et l'ajoute à la liste ouverte. La liste ouverte est une liste de nœuds qui sont en train d'être considérés pour expansion. L'algorithme répète les étapes suivantes jusqu'à ce que la liste ouverte soit vide.

1) L'algorithme récupère le nœud avec le coût le plus faible (valeur F) de la liste ouverte. La valeur F est une estimation du coût pour atteindre l'objectif à partir d'un nœud donné, en utilisant l'heuristique de distance de Manhattan.

Donc, tout d'abord, nous devons créer une implémentation Heap Tree to JPS

```python3
class HeapTree():
    def __init__(self):
        self.pq = []
        self.counter = itertools.count()

    def add_task(self, task, priority=0):
        'Add a new task'
        count = next(self.counter)
        entry = [priority, count, task]
        heapq.heappush(self.pq, entry)

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.pq) == 0
        
        .
        .
        .
        
def jump_point_search(field, start_y, start_x, end_y, end_x):
    .
    .
    .
        def queue_jumppoint(node):
            if node is not None:
                pq.add_task (node, field [node[0]] [node[1]] + max(abs(node[0] - end_x), abs(node[1] - end_y)))
```

2) Si le nœud est l'objectif, l'algorithme retourne le chemin du nœud de départ à l'objectif.

```python3
    class FoundPath(Exception):
        pass
```

3) Si le nœud n'est pas l'objectif, l'algorithme l'étend en générant ses successeurs. Un successeur est un nœud qui peut être atteint depuis le nœud courant en un seul pas.

```python3
    while (True):
        current_x += directionX
        current_y += directionY
        current_cost += 2**(1/2)

        if field[current_x][current_y] == BLANK:
            field[current_x][current_y] = current_cost
            sources[current_x][current_y] = startX, startY
        elif current_x == end_x and current_y == end_y:  # destination found
            field[current_x][current_y] = current_cost
            sources[current_x][current_y] = startX, startY
            raise FoundPath()
        else: #collided with an obstacle. We are done. 
            return None
    .
    .
    .
```

4) Pour chaque successeur, l'algorithme procède comme suit:

    a) Si le successeur est le but, l'algorithme renvoie le chemin du nœud de départ au but.
    
    b) Si le successeur n'est pas dans la liste ouverte ou fermée, l'algorithme l'ajoute à la liste ouverte et définit son parent sur le nœud courant. La liste fermée est une liste de nœuds qui ont déjà été étendus.
    
    c) Si le successeur est dans la liste ouverte, l'algorithme vérifie si le chemin actuel vers le successeur est meilleur que le chemin précédent. Si c'est le cas, l'algorithme met à jour le parent du successeur sur le nœud courant.

5) L'algorithme ajoute le nœud courant à la liste fermée.

```python3
while (not pq.empty()):
    pX, pY = pq.pop_task()

    try:
        queue_jumppoint(_jps_explore_cardinal(pX, pY, 1, 0))
        queue_jumppoint(_jps_explore_cardinal(pX, pY, -1, 0))
        queue_jumppoint(_jps_explore_cardinal(pX, pY, 0, 1))
        queue_jumppoint(_jps_explore_cardinal(pX, pY, 0, -1))

        queue_jumppoint(_jps_explore_diagonal(pX, pY, 1, 1))
        queue_jumppoint(_jps_explore_diagonal(pX, pY, 1, -1))
        queue_jumppoint(_jps_explore_diagonal(pX, pY, -1, 1))
        queue_jumppoint(_jps_explore_diagonal(pX, pY, -1, -1))
    except FoundPath:
        print("FoundPath Exception")
        return _get_path(sources, start_x, start_y, end_x, end_y)
```

#### Exemples

Supposons que nous ayons un point de départ vert et que nous voulions atteindre le point rouge.

À ce stade, l'algorithme commence à rechercher et nous obtenons : à partir du point vert, nous recherchons 8 directions ( haut, bas, gauche, droite, haut gauche, haut droite, bas gauche, bas droite ) et pour chaque direction, si la direction est diagonale, il balaye l'espace vertical et horizontal dans sa direction comme ci-dessous.

Ensuite, le chemin le plus court est renvoyé.

<div align="center"><img src="https://user-images.githubusercontent.com/54884571/210862898-bee6061a-aac5-43ba-b1ea-2a0894630f02.png" width ="50%"></div>

Pour un autre exemple avec un obstacle,

dans la première itération, l'algorithme n'a pas pu trouver le point rouge, il saute donc au coin qui est le coin le plus proche pour atteindre le point et continue à chercher à nouveau. Rappelez-vous que dans cette implémentation, faire avancer chaque unité coûte 1, faire avancer les diagonales coûte 2^(1/2).

<div align="center"><img src="https://user-images.githubusercontent.com/54884571/210863842-a0d3c691-33b0-47dd-9cbf-7d41b45f537a.png" width ="50%"></div>

<h2 id="results">Résultats</h2>

Lorsque nous exécutons l'ensemble du programme et que nous cliquons sur "Rechercher un itinéraire", nous pouvons obtenir les résultats de l'algorithme de recherche de points de saut.

<video src="https://user-images.githubusercontent.com/54884571/211015266-8f6135e4-65de-4e61-8874-00f2ba2a57f2.mp4" frameborder="0" allowfullscreen="true"></video>

<h2 id="conclusion">Conclusion</h2>

La recherche de points de saut est souvent utilisée dans les jeux vidéo et les applications robotiques où il est nécessaire de trouver le chemin le plus court dans un environnement basé sur une grille. Dans ces cas, JPS peut être utilisé pour trouver rapidement et efficacement un chemin à travers la grille tout en évitant les obstacles.

JPS est également utilisé dans d'autres applications où il est nécessaire de trouver le chemin le plus court à travers un graphique avec de nombreux chemins possibles, comme dans la planification des transports et de la logistique. Dans ces cas, l'algorithme peut être utilisé pour trouver l'itinéraire le plus efficace pour un camion de livraison ou un autre véhicule, en tenant compte de facteurs tels que les conditions de circulation et la structure du réseau routier.

Dans l'ensemble, JPS est un algorithme utile pour trouver un chemin le plus court à travers un graphique lorsque le graphique est grand ou lorsqu'il existe de nombreux chemins possibles qui doivent être pris en compte. Son efficacité le rend bien adapté pour une utilisation dans une variété d'applications où la recherche de trajectoire est importante.

<h2 id="references">Références</h2>

Un merci spécial à Daniel Harabor et Alban Grastien qui présentent formellement l'algorithme JPS et constituent une excellente référence lors de la mise en œuvre de l'algorithme par vous-même.

Merci également à Nathan Witmer qui a implémenté cet algorithme sur un site très explicatif et inspirant.

Enfin merci à mon meilleur ami pour les idées <img src="https://user-images.githubusercontent.com/54884571/210874888-ae0d86c5-f990-4f87-9556-2429ad1a8f64.png" height="14">

[1] https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-icaps14.pdf

[2] https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html
